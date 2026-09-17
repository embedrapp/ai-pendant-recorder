"""Quiet modular pendant. PCB-frame, millimeters; cloud build123d only."""
import json, os
from build123d import Box, Cylinder, RectangleRounded, Pos, Rot, Compound, extrude, fillet

def block(w,l,h,x,y,z): return Pos(x,y,z+h/2)*Box(w,l,h)
def rr(w,l,r,z,h,x=0,y=0): return Pos(x,y,z)*extrude(RectangleRounded(w,l,r),amount=h)
def hole(r,h,x,y,z): return Pos(x,y,z+h/2)*Cylinder(r,h)
def named(s,n):
    if isinstance(s,list): s=Compound(children=list(s))
    s.label=n
    return s
def gen_step():
    with open(os.environ['EMBEDR_MECHANICAL_PARAMETERS']) as f:p=json.load(f)
    with open(os.environ['EMBEDR_MECHANICAL_CONTEXT']) as f:c=json.load(f)
    bb=c['board']['bounds']; bw=bb['maxX']-bb['minX']; bl=bb['maxY']-bb['minY']
    assert abs(bw-36)<.01 and abs(bl-76)<.01,'Reassess mechanical interface for changed PCB'
    t=c['board']['thickness']['value']; wall=p['wall']; gap=p['board_gap']
    w=bw+2*(wall+gap); l=bl+2*(wall+gap)
    rear=p['rear_depth']; top=p['front_height']; seam=top-wall
    comps={a['ref']:a for a in c['components']}
    mounting=[h for h in c['board']['holes'] if h['ref'] in ['H1','H2','H3','H4']]
    outer=rr(w,l,5,-rear,rear+seam)
    outer=fillet([e for e in outer.edges() if abs(e.center().Z+rear)<.0001],p['edge_radius'])
    base=outer-rr(w-2*wall,l-2*wall,3.4,-rear+wall,rear+seam-wall+.2)
    lid=rr(w,l,5,seam+.2,wall)
    # Round only the exterior face perimeter before adding lips and openings.
    lid=fillet([e for e in lid.edges() if abs(e.center().Z-(top+.2))<.0001],p['edge_radius'])
    # Wearing orientation: +Y is lanyard/up, -Y is USB/ESP end/down.
    # +Z is outward LED face; -Z is battery/body-facing rear.
    # Labyrinth locating lip with trial-fit running clearance.
    lip=rr(w-2*wall-.6,l-2*wall-.6,3, seam-1.4,1.8)-rr(w-2*wall-2.6,l-2*wall-2.6,2,seam-1.5,2.1)
    lid+=lip
    pcb=rr(bw,bl,3,0,t)
    for h in mounting:
        x,y=h['center']['x'],h['center']['y']
        pcb-=hole(1.1,t+.2,x,y,-.1)
        base+=hole(2.1,rear-wall,x,y,-rear+wall)
        base-=hole(1.1,rear+.2,x,y,-rear-.1)
        base-=hole(2,1.0,x,y,-rear-.1)
        boss=hole(2.0,seam+.2-t,x,y,t)-hole(.8,seam-t-.8,x,y,t-.1)
        lid+=boss
    # USB bottom opening, provisional Z center measured from PCB datum.
    usb=Pos(0,-l/2+3,p['usb_z'])*Rot(90,0,0)*extrude(RectangleRounded(10,4.4,1.8),amount=6)
    base-=usb
    # Left microSD mouth plus shallow finger scallop. No lid removal required.
    sy=comps['J4']['pose']['y']+.095
    sd=block(6,12.4,2.5,-w/2,sy,t+.0)
    base-=sd
    base-=block(1.0,15,5,-w/2+.2,sy,t-1.0)
    # Recessed side slider opening; final contact travel must be bench verified.
    s2y=comps['SW2']['pose']['y']+2.5
    base-=block(6,7,3.4,w/2,s2y,p['slider_z']-.3)
    slider=block(1.2,4.2,2.4,w/2-.4,s2y,p['slider_z'])
    slider+=block(2.6,2.2,1.6,w/2-2.0,s2y,p['slider_z']+.4)
    slider-=block(2,1.8,1.2,w/2-2.8,s2y,p['slider_z']+.6)
    # Front record key respects top-actuated switch; no fictional side actuator.
    sx,sy1=comps['SW1']['pose']['x'],comps['SW1']['pose']['y']
    lid-=hole(2.4,wall+3,sx,sy1,seam-2)
    key=hole(2.1,wall+.7,sx,sy1,seam-.6)
    key+=hole(2.8,.6,sx,sy1,seam-.6)
    stem_z=t+p['record_height']+.2
    key+=hole(.9,seam-.6-stem_z,sx,sy1,stem_z)
    # Flush replaceable optical cassette and 25 separate light wells.
    led=[a for a in c['components'] if a['ref'].startswith('LED')]
    lx=sum(a['pose']['x'] for a in led)/25; ly=sum(a['pose']['y'] for a in led)/25
    lid-=rr(21,21,2,seam-2,wall+4,lx,ly)
    lens=rr(20.5,20.5,1.8,seam+.3,wall-.1,lx,ly)
    lens+=rr(23,23,2.5,seam-.5,.85,lx,ly)-rr(20,20,1.6,seam-.6,1.1,lx,ly)
    lid-=rr(23.4,23.4,2.7,seam-.7,1,lx,ly)
    baffle=rr(22.8,22.8,2.2,t+2, seam-.8-(t+2),lx,ly)
    for a in led:
        baffle-=block(3.2,3.2,top,a['pose']['x'],a['pose']['y'],t+1.9)
    # Battery is behind PCB, never in the optical path. Removable insulated sled.
    by=8; floor=-rear+wall+.3
    tray=rr(32.4,38.4,1.2,floor,.8,0,by)
    tray+=block(.9,38.4,3,-15.75,by,floor+.8)
    tray+=block(.9,38.4,3,15.75,by,floor+.8)
    tray+=block(32.4,.9,3,0,by-18.75,floor+.8)
    tray+=block(22,.9,3,0,by+18.75,floor+.8)
    # Open lead exit, pull-tab notch and non-compressive strap slots.
    for xx in (-14,14):tray-=block(1.4,8,1.2,xx,by,floor-.1)
    battery=block(30.1,36,5.1,0,by,floor+.9)
    assert floor+.9+6.1 < -1.0,'Battery expansion reserve reaches board'
    # Bottom-port microphone: rear bore and isolated acoustic chimney, clear of cell.
    mh=next(h for h in c['board']['holes'] if h['ref']=='MK1')
    mx,my=mh['center']['x'],mh['center']['y']
    base+=hole(1.5,rear-wall-.4,mx,my,-rear+wall)
    base-=hole(.6,rear+.2,mx,my,-rear-.1)
    seal=hole(1.4,.4,mx,my,-.4)-hole(.6,.6,mx,my,-.5)
    # Flush rear lanyard bridge kept outside battery chamber.
    base-=block(9,3,2,0,31,-rear-.1)
    base+=block(12,1.6,2.5,0,33,-rear+wall)
    parts=[named(base,'01 Rear chassis — PA12'),named(lid,'02 Front cover — PA12'),
      named(tray,'03 Removable battery sled'),named(lens,'04 Flush diffuser cassette'),
      named(baffle,'05 Optical isolation grid'),named(key,'06 Captive record key'),
      named(slider,'07 Standby slider'),named(seal,'08 Microphone gasket'),
      named(pcb,'REFERENCE actual PCB envelope'),named(battery,'REFERENCE battery 30.1x36x5.1')]
    # Reference components are deliberately envelopes, not purported exact models.
    for ref,height in [('U1',4),('J4',1.42),('J1',8),('J3',8)]:
        a=comps[ref];e=a['envelope2d']
        if ref=='J4':
            shape=block(11.4,11.95,height,-11.4,21,t)
        else:shape=block(e['maxX']-e['minX'],e['maxY']-e['minY'],height,(e['minX']+e['maxX'])/2,(e['minY']+e['maxY'])/2,t)
        parts.append(named(shape,'REFERENCE '+ref+' provisional envelope'))
    # Normalize Boolean results (which may be ShapeLists) into labelled solids.
    solids=[]
    for part in parts:
        for solid in part.solids():
            solid.label=part.label
            solids.append(solid)
    return Compound(children=solids)