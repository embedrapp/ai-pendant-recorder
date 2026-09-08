"""Development enclosure. Coordinates are proposed, NOT extracted port locations.
Only the cloud worker executes this generator. PCB bottom is Z=0.
"""
import json
import os
from build123d import Box, Cylinder, RectangleRounded, Pos, Rot, Compound, Part, extrude


def rounded(w, l, r, z, h):
    return Pos(0, 0, z) * extrude(RectangleRounded(w, l, r), amount=h)


def box(w, l, h, x, y, z):
    return Pos(x, y, z + h / 2) * Box(w, l, h)


def cyl(r, h, x, y, z):
    return Pos(x, y, z + h / 2) * Cylinder(r, h)


def volume_of(shape):
    if shape is None:
        return 0.0
    if hasattr(shape, 'volume'):
        return shape.volume
    return sum(s.volume for s in shape)


def gen_step() -> Compound:
    with open(os.environ['EMBEDR_MECHANICAL_PARAMETERS'], encoding='utf-8') as f:
        p = json.load(f)
    with open(os.environ['EMBEDR_MECHANICAL_CONTEXT'], encoding='utf-8') as f:
        context = json.load(f)  # retained for revision provenance, not asserted as fitted
    w, l, t = p['width'], p['length'], p['wall']
    rear, front, gap = p['rear_z'], p['front_z'], p['fit_gap']
    seam = front - t
    floor = -rear + p.get('floor_thickness', 2.0)
    # Soft plan-view corners, uninterrupted front except functional apertures.
    base = rounded(w, l, 5, -rear, seam + rear)
    base -= rounded(w - 2*t, l - 2*t, 5-t, floor, seam-floor+0.2)
    lid = rounded(w, l, 5, seam, t)
    # Slip-fit internal locating skirt; no unqualified snap-fit claims.
    skirt = rounded(w-2*t-2*gap, l-2*t-2*gap, 5-t-gap, seam-1.6, 1.6)
    skirt -= rounded(w-2*t-2*gap-1.6, l-2*t-2*gap-1.6, 5-t-gap-0.8, seam-1.7, 1.9)
    lid += skirt
    holes = [h for h in context['board']['holes'] if h.get('ref') in ('H1','H2','H3','H4')]
    assert len(holes) == 4, 'Expected four carrier mounting holes'
    for hole in holes:
        x, y = hole['center']['x'], hole['center']['y']
        if True:
            base += cyl(2.2, -floor, x, y, floor)
            base -= cyl(0.75, -floor+0.05, x, y, floor+0.5)
            lid += cyl(2.2, seam-1.62+0.05, x, y, 1.62)
            lid -= cyl(1.1, front-1.62+0.2, x, y, 1.52)
            lid -= cyl(1.85, 0.85, x, y, front-0.75)
    # Camera deliberately omitted. Legacy camera parameters are inert so older
    # saved parameter sets remain readable. Mic alignment still requires metrology.
    mx, my = p['mic_x'], p['mic_y']
    lid += cyl(2.4, 0.9, mx, my, seam-0.9)
    lid -= cyl(0.6, t+1.3, mx, my, seam-1.0)
    # Fine 0.9 mm dot field over the speaker; blind gasket seat underneath.
    sy = p.get('speaker_y', -16)
    for row in range(-2, 3):
        for col in range(-4, 5):
            x, y = col*1.6, row*1.6
            if abs(x) <= 6.4:
                lid -= cyl(0.45, t+0.4, x, sy+y, seam-0.2)
    ring = box(18.6, 11.6, 3.5, 0, sy, seam-3.5) - box(16.6, 9.6, 3.7, 0, sy, seam-3.6)
    ring -= box(3, 4, 2, 0, sy+5.5, seam-3.5)  # speaker lead escape
    lid += ring
    # USB on top edge; SD is deliberately lid-off service to avoid an open slot.
    base -= box(10, 5, 4.5, 0, l/2-1, 2)
    # Recessed side access, pending exact switch/button packages.
    base -= box(5, 7, 3, w/2-1, -7, 3)
    sw = next(c for c in context['components'] if c['ref'] == 'SW1')
    base -= box(6, 3.2, 2.6, w/2-1, sw['pose']['y'], 1.4)
    # Flat LiPo holder: open-top non-compressive tray, cable notch, strap windows.
    tray = rounded(28, 44, 2, floor+0.15, 6.0)
    tray -= rounded(26, 42, 1, floor+1.15, 5.6)
    tray -= box(7, 4, 4, 0, 21, floor+1.65)
    for x in (-13.5, 13.5):
        tray -= box(4, 9, 1.4, x, 0, floor+1.0)
    # Four bounded tray locator lugs; tray lifts out after PCB removal.
    for y in (-23, 23):
        base += box(10, 0.8, 1.3, 0, y, floor)
    # Blind magnet seats accessed from inside. Adhesive/captive coating required.
    for x in (-9, 9):
        for y in (-25, 25):
            base -= cyl(2.15, 1.1, x, y, floor-1.05)
    # Integrated neck-cord bail, behind the USB opening (which starts at Z=2).
    # Flat rear face permits shell-floor-down printing; rounded planar edges.
    bail_width = p.get('cord_loop_width', 12.0)
    bail_hole = p.get('cord_loop_opening', 6.0)
    bail_depth = p.get('cord_loop_thickness', 3.0)
    bail = Pos(0, l/2+3, 0) * rounded(bail_width, 12, 4, -rear, bail_depth)
    cord_void = Pos(0, l/2+4, 0) * rounded(bail_hole, 6, 2, -rear-0.1, bail_depth+0.2)
    base += bail
    base -= cord_void
    assert volume_of(base & cord_void) < 0.001, 'Neck cord opening obstructed'
    # Separate clothing backer, 1.5 mm fabric gap; pockets on garment-facing side.
    bz = -rear-4.5
    backer = rounded(w-4, l-10, 5, bz, 3)
    for x in (-9, 9):
        for y in (-25, 25):
            backer -= cyl(2.15, 1.15, x, y, bz+1.9)
    # Hidden lanyard tunnel through upper backer, generous material around it.
    backer -= Pos(0, l/2-8, bz+1.5) * Rot(0, 90, 0) * Cylinder(0.9, w)
    # Normalize boolean results into Parts before assembly (disjoint solids may
    # be returned as ShapeList by the worker's build123d release).
    base = Part(children=list(base.solids())) if hasattr(base, 'solids') else Part(children=list(base))
    lid = Part(children=list(lid.solids())) if hasattr(lid, 'solids') else Part(children=list(lid))
    tray = Part(children=list(tray.solids())) if hasattr(tray, 'solids') else Part(children=list(tray))
    backer = Part(children=list(backer.solids())) if hasattr(backer, 'solids') else Part(children=list(backer))
    base.label = 'Rear shell — integrated neck cord loop, PCB standoffs and magnet pockets'
    lid.label = 'Front — camera-free, isolated mic port, speaker dot grid'
    tray.label = 'Removable LiPo tray — no cell clamping'
    backer.label = 'Clothing backer — magnetic and lanyard attachment'
    parts = {'rear-shell': base, 'lid': lid, 'battery-tray': tray, 'clothing-backer': backer}
    for name, part in parts.items():
        assert len(part.solids()) == 1, name + ': must be one connected solid'
        assert part.is_valid, name + ': invalid B-rep'
        assert part.volume > 1, name + ': empty geometry'
    # A continuous central volume extends from the floor through the open rim.
    # Unlike a bounding box or solid count, this detects an accidental cavity cap.
    cavity_probe = box(20, 36, seam-floor+1, 0, 0, floor+0.01)
    assert volume_of(base & cavity_probe) < 0.001, 'Rear cavity is obstructed'
    assert volume_of(base & box(20, 36, 0.2, 0, 0, -rear+0.1)) > 143, 'Rear floor missing'
    for a, b in [('rear-shell', 'lid'), ('rear-shell', 'battery-tray'),
                 ('rear-shell', 'clothing-backer'), ('lid', 'battery-tray')]:
        assert volume_of(parts[a] & parts[b]) < 0.001, a + '/' + b + ': interference'
    # Reserved cell envelope includes provisional expansion allowance, not a
    # supplier-certified pack dimension. Reject builds with insufficient tail gap.
    cell_height = p.get('battery_reserved_height', 6.0)
    tail_depth = p.get('tail_below_board', 2.5)
    cell_top = floor + 1.15 + cell_height
    assert -tail_depth-cell_top >= 1.0, 'Battery/solder-tail clearance below 1 mm'
    # Reserve a conservative mated battery-connector volume. Its height and
    # lead exit remain assembly acceptance limits, not measured part facts.
    j1 = next(c for c in context['components'] if c['ref'] == 'J1')
    e = j1['envelope2d']
    plug = box(e['maxX']-e['minX']+1, e['maxY']-e['minY']+2,
               9, (e['maxX']+e['minX'])/2, (e['maxY']+e['minY'])/2, 1.62)
    assert volume_of(lid & plug) < 0.001, 'Mated battery connector intersects lid'
    for c in context['components']:
        for pad in c.get('pads', []):
            if pad.get('padType') == 'thru_hole':
                x, y = pad['center']['x'], pad['center']['y']
                tail = cyl(0.8, tail_depth, x, y, -tail_depth)
                assert volume_of(tray & tail) < 0.001, 'Tail intersects tray: ' + c['ref']
    selected = p.get('export_part', 'assembly')
    if selected != 'assembly':
        part = parts[selected]
        # Lid outer face on the build plane; the other parts open upward.
        if selected == 'lid':
            part = Rot(180, 0, 0) * part
        part = Pos(0, 0, -part.bounding_box().min.Z) * part
        part.label = selected
        return part
    if p['exploded']:
        lid = Pos(2*(w+10), 0, front) * Rot(180, 0, 0) * lid
        tray = Pos(w+10, 0, 0) * tray
        backer = Pos(-w-10, 0, 0) * backer
    model = Compound(list(base.solids()) + list(lid.solids()) + list(tray.solids()) + list(backer.solids()))
    return model