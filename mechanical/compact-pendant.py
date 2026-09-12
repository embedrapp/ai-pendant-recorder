"""Modular fit prototype, PCB frame. Only executed on the mechanical worker."""
import json, os
from build123d import Box, Cylinder, RectangleRounded, Pos, Rot, Compound, extrude, fillet, Helix, Plane, Circle, sweep

def block(w,l,h,x,y,z):
    return Pos(x,y,z+h/2)*Box(w,l,h)
def roundbox(w,l,r,z,h):
    return Pos(0,0,z)*extrude(RectangleRounded(w,l,r),amount=h)
def bore(r,h,x,y,z):
    return Pos(x,y,z+h/2)*Cylinder(r,h)
def gen_step():
    with open(os.environ['EMBEDR_MECHANICAL_PARAMETERS']) as f: p=json.load(f)
    with open(os.environ['EMBEDR_MECHANICAL_CONTEXT']) as f: c=json.load(f)
    # Preserve enclosure datums relative to KiCad (100,100), then transform
    # the result back into the current outline-centered canonical frame.
    frame_shift=100-c['frame']['origin']['kicadY']
    for h in c['board']['holes']: h['center']['y']+=frame_shift
    for comp in c['components']:
        comp['pose']['y']+=frame_shift
        if comp.get('envelope2d'):
            comp['envelope2d']['minY']+=frame_shift
            comp['envelope2d']['maxY']+=frame_shift
    w,l,t=p['width'],p['length'],p['wall']
    rear,front,g=p['rear_z'],p['front_z'],p['fit_gap']
    shell_y=p.get('shell_y',0)
    top_y=shell_y+l/2; bottom_y=shell_y-l/2
    floor=-rear+p['floor_thickness']; seam=front-t
    # R5 plan corners retain actual corner mounting clearances.
    outer=Pos(0,shell_y,0)*roundbox(w,l,5,-rear,seam+rear)
    bottom_edges=[e for e in outer.edges() if abs(e.center().Z+rear)<.01]
    outer=fillet(bottom_edges,1.2)
    base=outer-Pos(0,shell_y,0)*roundbox(w-2*t,l-2*t,5-t,floor,seam-floor+.1)
    lid=Pos(0,shell_y,0)*roundbox(w,l,5,seam,t)
    lid=fillet([e for e in lid.edges() if abs(e.center().Z-front)<.01],.8)
    skirt=roundbox(w-2*t-2*g,l-2*t-2*g,5-t-g,seam-1.5,1.5)
    skirt-=roundbox(w-2*t-2*g-2,l-2*t-2*g-2,4-t-g,seam-1.6,1.7)
    lid+=Pos(0,shell_y,0)*skirt
    holes=[h for h in c['board']['holes'] if h['ref'] in ('H1','H2','H3','H4')]
    assert len(holes)==4
    for h in holes:
        x,y=h['center']['x'],h['center']['y']
        base+=bore(2.3,-floor,x,y,floor)
        # Rear-entry M2-class thread-forming screws: clearance through base
        # and PCB, blind pilot in front-cover post. Front skin stays intact.
        head_depth=1.3
        base-=bore(1.1,rear+.2,x,y,-rear-.1)
        base-=bore(2.1,head_depth+.1,x,y,-rear-.1)
        board_top=c['board']['thickness']['value']
        lid+=bore(1.8,seam-board_top+.1,x,y,board_top)
        lid-=bore(.8,7.4,x,y,board_top-.1)
        # Candidate 12 mm under-head length, low-profile head <=1.2 mm.
        tip=-rear+head_depth+12
        assert board_top+4<tip<board_top+7.0, 'Rear screw engagement / blind-tip allowance'
        assert front-(board_top+7.3)>1.2, 'Front skin above blind pilot'
    # Rounded 10 x 4.2 USB mouth; height remains a metrology parameter.
    base-=Pos(0,bottom_y+3,4.2)*Rot(90,0,0)*extrude(RectangleRounded(10,4.2,2),amount=6)
    # Captive recording button: rounded external face, inner stop flange.
    controls={comp['ref']:comp for comp in c['components']}
    # Retain provisional tip offset, derive position from revised PCB.
    sy=controls['SW1']['pose']['y']; sz=2.9
    tip=controls['SW1']['pose']['x']+2.15+.15
    slot=Pos(w/2-3,sy,sz)*Rot(0,90,0)*extrude(RectangleRounded(3.2,6.6,1.4),amount=6)
    base-=slot
    pusher=Pos(w/2-.8,sy,sz)*Rot(0,90,0)*extrude(RectangleRounded(2.6,6,1.2),amount=1)
    pusher+=block(w/2-.8-tip,1.5,1.5,(w/2-.8+tip)/2,sy,sz-.75)
    pusher+=block(.7,8,4,w/2-t-.65,sy,sz-2)
    # Two cantilever return tabs; trial-print force and fatigue are NOT verified.
    for sign in (-1,1):
        pusher+=block(.6,5,1,w/2-t-.65,sy+sign*5.5,sz-.5)
        base+=block(1,1.2,2,w/2-t-.5,sy+sign*8.6,sz-1)
    # Captive SW2 extension: fit-prototype 2 mm throw and actuator Z envelope.
    # F.Fab gives 1.5 mm actuator width, 2 mm projection, center offsets 1.5/3.5.
    s2y=controls['SW2']['pose']['y']+2.5
    s2x=controls['SW2']['pose']['x']
    inner=w/2-t
    base-=block(8,6.6,2.6,w/2,s2y,2.2)
    slider=block(w/2+.5-(s2x+4.1),3.8,2,(w/2+.5+s2x+4.1)/2,s2y-1,2.5)
    slider+=block(.7,3.8,3.4,inner-.65,s2y-1,1.8)
    # Open inward socket captures actuator laterally; installed before PCB.
    slider-=block(3,2.1,2.6,s2x+4.7,s2y-1,2.2)
    for sign in (-1,1):
        base+=block(1.8,9,1,w/2+.4,s2y,3.5+sign*2.2-.5)
    # Check the complete translational sweep against shell, not just one pose.
    for dy in (0,.5,1,1.5,2):
        contact=base.intersect(Pos(0,dy,0)*slider)
        assert contact is None or sum(s.volume for s in contact.solids())<.001, 'SW2 slider travel blocked'
    # microSD is serviced with lid removed: no giant side-wall opening.
    # Antenna mount on upper inner wall, no surrounding metal features.
    # Plastic only, radiating face outward; footprint/cable must be measured.
    antenna_shelf=block(1.2,6,8,-w/2+t+.6,54,2)
    base+=antenna_shelf
    # Front-directed light guides above top-emitting edge LEDs; 0.9 mm dots.
    inserts=[]
    for ref in ('D2','D3'):
        x=controls[ref]['pose']['x']; y=controls[ref]['pose']['y']
        lid-=bore(.45,t+1,x,y,seam-.2)
        baffle=bore(1.2,seam-2.8,x,y,2.8)-bore(.7,seam-2.6,x,y,2.7)
        lid+=baffle
        insert=bore(.45,front-2.9,x,y,2.9)
        insert.label='LED light insert '+str(y);inserts.append(insert)
    # Front battery tray for stocked Adafruit 1578 / PKCELL 500 mAh pack,
    # stacked above the PCB. The supplier page reports 29 x 36 x 4.75 mm,
    # while its pack drawing gives 30 +/-0.1 x 35 +/-0.1 x 5 +/-0.1 mm.
    # Use the conservative union: 30.1 x 36.0 x 5.1 mm. The 6.1 mm Z
    # envelope adds 1.0 mm expansion allowance; the low rim
    # locates the pack without clamping its broad faces or swollen pouch.
    by=p.get('battery_y',20); tz=p.get('tray_z',5.2)
    battery_w,battery_l,battery_h=30.1,36.0,6.1
    cavity_w,cavity_l=30.6,36.5
    tray_w,tray_l=32.2,38.1
    tray=Pos(0,by,0)*roundbox(tray_w,tray_l,2,tz,1.2)
    # Keep the cavity rectangular so the complete maximum drawing envelope,
    # including its corners, remains clear of the locating rim.
    rim=roundbox(tray_w,tray_l,2,tz+1.2,1.6)-block(cavity_w,cavity_l,1.8,0,0,tz+1.1)
    tray+=Pos(0,by,0)*rim
    # Lead notch faces J1/speaker end. The 100 mm lead is service-looped in
    # the shell; the pouch tabs and PCM remain supported by the tray floor.
    tray-=block(10,5,4,0,by+tray_l/2,tz+1.2)
    # The lower rim remains separated from the camera aperture envelope.
    # Pull-release adhesive strips go on the floor, not on pouch edges.
    for h in holes:
        tray-=bore(2.65,12,h['center']['x'],h['center']['y'],tz-.1)
    # Side shelves support tray independently of cell and PCB components.
    for x in (-17,17):
        # Side shelf above PCB; outer spine joins shell without piercing PCB.
        base+=block(3,3,tz-2,x,48,2)
        base+=block(1.2,3,tz-floor,(w/2-t) if x>0 else -(w/2-t),48,floor)
        base+=block(2,3,tz-2,(x+((w/2-t) if x>0 else -(w/2-t)))/2,48,2)
        tray+=block(3,4,1.2,x,47.5,tz)
        base-=bore(.8,3,x,48,tz-2.8)
        tray-=bore(1.1,2,x,48,tz-.1)
    # Camera aperture and microphone: explicitly adjustable provisional datums.
    cx,cy=p['camera_x'],p['camera_y']
    lid-=bore(p['camera_radius'],t+1,cx,cy,seam-.2)
    lid-=bore(.65,t+1,p['mic_x'],p['mic_y'],seam-.2)
    # Coaxial removable screw cap: no rails, frame or raised handle.
    # Custom round thread, NOT an ISO/M-series interchangeable thread.
    pitch=p.get('cap_pitch',1.5); clearance=p.get('cap_thread_clearance',.25)
    aperture=p['camera_radius']; root=aperture+1.0
    cap_r=root+1.8; bead=.45; thread_r=root-.05
    collar_h=2.9; roof_z=front+3.2; cap_top=roof_z+1.0
    path=Helix(pitch=pitch,height=2.0,radius=thread_r)
    profile_plane=Plane(origin=path@0,z_dir=path%0)
    male=sweep(profile_plane*Circle(bead),path=path,is_frenet=True)
    # Extend the female helix below its open mouth: a blind-ended groove jams
    # during unscrewing even when its seated Boolean clearance is clean.
    female_path=Helix(pitch=pitch,height=2.0+pitch,radius=thread_r)
    groove=Pos(0,0,-pitch)*sweep(Plane(origin=female_path@0,z_dir=female_path%0)*Circle(bead+clearance),path=female_path,is_frenet=True)
    thread_pose=Pos(cx,cy,front+.55)
    collar=bore(root,collar_h+.1,cx,cy,front-.1)+thread_pose*male
    collar-=bore(aperture,collar_h+.4,cx,cy,front-.2)
    lid+=collar
    cap=bore(cap_r,cap_top-front,cx,cy,front)
    cap=fillet([e for e in cap.edges() if abs(e.center().Z-cap_top)<.01],.45)
    cap-=bore(root+clearance,roof_z-front+.2,cx,cy,front-.2)
    cap-=thread_pose*groove
    # Shallow coin/fingernail slot leaves 0.65 mm opaque roof, no handle.
    cap-=Pos(cx,cy,cap_top-.35)*extrude(RectangleRounded(7,1.2,.55),amount=.5)
    assert len(cap.solids())==1 and cap.is_valid, 'Cap must be one valid printable solid'
    # Test seated and sampled right-handed unscrewing poses against complete lid.
    for angle in (0,45,90,180,360,720,900):
        moving=Pos(cx,cy,pitch*angle/360)*Rot(0,0,angle)*Pos(-cx,-cy,0)*cap
        overlap=lid.intersect(moving)
        volume=0 if overlap is None else sum(s.volume for s in overlap.solids())
        assert volume<.001, 'Cap/lid collision at '+str(angle)+' degrees: '+str(volume)
    # True top-edge speaker, radiating along +Y toward the neck, not +Z.
    sx,sy=0,top_y-t
    speaker_pose=Pos(sx,sy,10)*Rot(-90,0,0)
    for a in range(-4,5):
        for b in range(-2,3): base-=speaker_pose*bore(.5,t+1,a*1.7,b*1.7,-.2)
    seat=speaker_pose*(block(19,12,1.5,0,0,-1.5)-block(16.6,9.6,2,0,0,-1.7))
    base+=seat
    retainer=speaker_pose*(block(20,13,1.2,0,0,-5)-block(14,7,1.6,0,0,-5.2))
    # Screw seats for removable speaker clamp (pilot holes, print-calibrate).
    for x in (-10.5,10.5):
        base+=speaker_pose*bore(2,5,x,0,-5)
        base-=speaker_pose*bore(.7,4.5,x,0,-5.1)
        retainer+=speaker_pose*bore(2,1.2,x,0,-5)
        retainer-=speaker_pose*bore(.9,1.5,x,0,-5.1)
    # Motor cradle below lid, outside camera/speaker/antenna zones.
    # Move haptic cradle below the upper speaker/clamp envelope.
    mx,my=12,39
    cradle=bore(6,3.0,mx,my,floor)-bore(5.25,3.9,mx,my,floor-.1)
    cradle-=block(3,8,4,mx,my-5,floor-.1)
    # Rear motor seat ends 0.5 mm below PCB; motor thickness remains provisional.
    base+=cradle
    speaker_envelope=speaker_pose*block(16.6,9.6,3.5,0,0,-5)
    for label,a,b in [('speaker-base',speaker_envelope,base),
                      ('speaker-motor',speaker_envelope,cradle),
                      ('clamp-motor',retainer,cradle),('speaker-cap',speaker_envelope,cap)]:
        common=a.intersect(b)
        volume=0 if common is None else sum(s.volume for s in common.solids())
        assert volume<.001, label+' interference mm3: '+str(volume)
    assert abs(sx)<.001, 'Top grille must remain centered'
    # Reinforced loop integrated into upper-left shell. Smooth through hole.
    loop=Pos(0,top_y-1,0)*roundbox(10,7,3,-rear,3)
    loop-=bore(1.8,4,0,top_y,-rear-.2)
    base+=loop
    # Blind magnet pockets and removable clothing backer; glue + mechanical caps.
    for y in (-12,12): base-=bore(3.15,1.3,0,y,-rear-.01)
    backer=roundbox(17,37,5,-rear-4,2)
    for y in (-12,12): backer-=bore(3.15,1.2,0,y,-rear-3.1)
    parts={'rear-shell':base,'lid':lid,'battery-tray':tray,'record-pusher':pusher,
           'privacy-cap':cap,'speaker-retainer':retainer,'clothing-backer':backer,'standby-slider':slider}
    for name,obj in parts.items(): obj.label=name
    # Explicit engineering envelopes, never presented as verified component models.
    bounds=c['board']['bounds']
    # Exact rounded-rectangle containment of conservative 2D envelopes.
    # This supplements the placement tool's unsupported-arc result.
    hw=(bounds['maxX']-bounds['minX'])/2
    hl=(bounds['maxY']-bounds['minY'])/2
    for comp in c['components']:
        e=comp.get('envelope2d')
        if not e: continue
        if comp['ref']=='SW2':
            # Intentional actuator/courtyard overhang only. Actual 1.4 mm pads
            # and F.Fab body remain inside; no blanket containment waiver.
            assert comp['pose']['x']+3.65<hw
            assert comp['pose']['x']+5.65>hw
            assert all(pad['center']['x']+.7<hw for pad in comp['pads'])
            continue
        for x in (e['minX'],e['maxX']):
            for y in (e['minY'],e['maxY']):
                dx=max(abs(x)-(hw-3),0)
                dy=max(abs(y-frame_shift)-(hl-3),0)
                assert dx*dx+dy*dy<9, 'Envelope outside R3 PCB: '+comp['ref']
    pcb=Pos(0,frame_shift,0)*roundbox(bounds['maxX']-bounds['minX'],bounds['maxY']-bounds['minY'],3,0,c['board']['thickness']['value'])
    for h in holes:
        pcb-=bore(h['drillDiameter']/2,2,h['center']['x'],h['center']['y'],-.1)
    battery=block(battery_w,battery_l,battery_h,0,by,tz+1.2)
    refs=[pcb,battery,speaker_envelope]
    for comp in c['components']:
        if comp['ref'].startswith('H') or comp['ref'].startswith('TP'): continue
        e=comp.get('envelope2d')
        if not e: continue
        height=15 if comp['ref']=='U1' else (7 if comp['ref'] in ('J1','J3') else 3 if comp['ref'].startswith(('J','SW')) else 1)
        refs.append(block(e['maxX']-e['minX'],e['maxY']-e['minY'],height,(e['maxX']+e['minX'])/2,(e['maxY']+e['minY'])/2,1.62))
    for name,a,b in [('battery-tray',battery,tray),('battery-lid',battery,lid),('tray-lid',tray,lid),('tray-shell',tray,base),('battery-speaker',battery,speaker_envelope)]+[('tray-component-'+str(i),tray,r) for i,r in enumerate(refs[3:])]+[('battery-component-'+str(i),battery,r) for i,r in enumerate(refs[3:])]:
        common=a.intersect(b)
        volume=0 if common is None else sum(s.volume for s in common.solids())
        assert volume<.001, name+' interference mm3 '+str(volume)
    for label,a,b in [('shell-tray',base,tray),('shell-lid',base,lid),('shell-pusher',base,pusher),('pcb-shell',pcb,base),('pcb-lid',pcb,lid),('cell-tray',battery,tray)]:
        common=a.intersect(b)
        volume=0 if common is None else sum(s.volume for s in common.solids())
        print('FIT_INTERSECTION_MM3',label,round(volume,5))
    selection=p.get('export_part','assembly')
    if selection=='unified-pcb':
        # Fuse the same positioned envelopes shown in the assembly cutaway.
        # Battery and off-board speaker stay separate, as in the real stack.
        populated=pcb
        for envelope in refs[3:]:
            populated=populated.fuse(envelope)
        assert populated.is_valid and len(populated.solids())==1, 'Unified PCB must be one solid'
        populated.label='REFERENCE populated PCB - provisional component envelopes'
        return Pos(0,-frame_shift,0)*populated
    if selection=='print-kit':
        # Separate, bed-zeroed parts on a 100 mm grid for lossless identification
        # after cloud tessellation. No local CAD execution is needed.
        kit=dict(parts)
        kit['light-insert-D2']=inserts[0]
        kit['light-insert-D3']=inserts[1]
        dummy_pcb=pcb
        for h in c['board']['holes']:
            if h['ref'] not in ('H1','H2','H3','H4'):
                dummy_pcb-=bore(h['drillDiameter']/2,2,h['center']['x'],h['center']['y'],-.1)
        kit['REFERENCE-PCB']=dummy_pcb
        kit['REFERENCE-Adafruit-1578-max-30.1x36x5.1']=block(30.1,36,5.1,0,0,0)
        kit['REFERENCE-Adafruit-1578-reserved-30.1x36x6.1']=block(30.1,36,6.1,0,0,0)
        kit['REFERENCE-speaker-16.6x9.6x3.5']=block(16.6,9.6,3.5,0,0,0)
        kit['REFERENCE-motor-10x2.7']=bore(5,2.7,0,0,0)
        for comp in sorted(c['components'],key=lambda a:a['ref']):
            if comp['ref'].startswith(('H','TP')): continue
            e=comp.get('envelope2d')
            if not e: continue
            height=15 if comp['ref']=='U1' else (7 if comp['ref'] in ('J1','J3') else 3 if comp['ref'].startswith(('J','SW')) else 1)
            kit['REFERENCE-'+comp['ref']+'-envelope']=block(e['maxX']-e['minX'],e['maxY']-e['minY'],height,0,0,0)
        shapes=[]
        for i,(name,obj) in enumerate(kit.items()):
            b=obj.bounding_box()
            obj=Pos(100*(i%8)-(b.min.X+b.max.X)/2,100*(i//8)-(b.min.Y+b.max.Y)/2,-b.min.Z)*obj
            obj.label=name
            shapes.append(obj)
            print('PRINT_KIT_ITEM',i,name)
        return Compound(shapes)
    if selection=='cutaway':
        cut=block(w+10,l+10,70,w/2+5,0,-25)
        shapes=[base-cut,lid-cut,tray-cut,pusher,slider]+refs
        return Pos(0,-frame_shift,0)*Compound([solid for shape in shapes for solid in shape.solids()])
    if selection in parts: return Pos(0,-frame_shift,0)*parts[selection]
    # Exploded presentation preserves separately printable bodies, not a fit verdict.
    dz=p.get('explode',0)
    cap_lift=p.get('cap_lift',0)
    shapes=[base,tray,pusher,slider,Pos(0,0,dz)*lid,Pos(0,0,dz+cap_lift)*cap,
            Pos(0,0,dz)*retainer,backer]+inserts
    return Pos(0,-frame_shift,0)*Compound([solid for shape in shapes for solid in shape.solids()])