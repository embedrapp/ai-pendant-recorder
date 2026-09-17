"""Board-only silkscreen cleanup; run with KiCad's Python. No placement changes."""
import pcbnew as k
import json, shutil
from pathlib import Path
p=Path('pcb/layout/layout.kicad_pcb')
backup=p.with_suffix('.pre-silk.kicad_pcb')
if not backup.exists(): shutil.copy2(p,backup)
b=k.LoadBoard(str(p))
def box(r,margin=0):
    return (k.ToMM(r.GetX())-margin,k.ToMM(r.GetY())-margin,k.ToMM(r.GetRight())+margin,k.ToMM(r.GetBottom())+margin)
def overlap(a,z):return a[0]<z[2] and a[2]>z[0] and a[1]<z[3] and a[3]>z[1]
def position(t,x,y):t.SetPosition(k.VECTOR2I(k.FromMM(x),k.FromMM(y)))
obstacles=[]
for f in b.GetFootprints():
    for pad in f.Pads(): obstacles.append(box(pad.GetBoundingBox(),.25))
    # Avoid printing under component bodies/courtyards.
    courtyard=[box(g.GetBoundingBox(),.15) for g in f.GraphicalItems() if g.GetLayer()==k.F_CrtYd]
    if courtyard: obstacles.append((min(r[0] for r in courtyard),min(r[1] for r in courtyard),max(r[2] for r in courtyard),max(r[3] for r in courtyard)))
# Retain nonprinting identity for every part; reserve silk for readable references.
placed=[]; hidden=[]; shown=[]
for f in sorted(b.GetFootprints(),key=lambda f:(not f.GetReference().startswith(('J','SW','U','MK','TP')),f.GetReference())):
    t=f.Reference();t.SetLayer(k.F_SilkS);t.SetVisible(True)
    t.SetTextSize(k.VECTOR2I(k.FromMM(.8),k.FromMM(.8)));t.SetTextThickness(k.FromMM(.12))
    t.SetTextAngle(k.EDA_ANGLE(0,k.DEGREES_T))
    x,y=k.ToMM(f.GetPosition().x),k.ToMM(f.GetPosition().y)
    candidates=[]
    # Uniform horizontal labels, nearby only; do not imply distant associations.
    for dist in [1.6,2.1,2.7,3.3,4.0]:
        candidates += [(x,y-dist),(x,y+dist),(x-dist,y),(x+dist,y)]
    if f.GetReference()=='J4': candidates=[(88.5,68.5)]+candidates
    if f.GetReference()=='U1': candidates=[(100,96)]+candidates
    for xx,yy in candidates:
        position(t,xx,yy);r=box(t.GetBoundingBox(),.15)
        if r[0]<82.6 or r[2]>117.4 or r[1]<44.7 or r[3]>119.3:continue
        if any(overlap(r,z) for z in obstacles+placed):continue
        placed.append(r);shown.append(f.GetReference());break
    else:
        t.SetLayer(k.F_Fab);position(t,x,y);hidden.append(f.GetReference())
    # Values belong in the assembly drawing, not the printed board.
    f.Value().SetLayer(k.F_Fab)
# Relocate only pad-colliding silk graphics to fabrication, retaining geometry.
moved=0
for f in b.GetFootprints():
    for g in f.GraphicalItems():
        if g.GetLayer()!=k.F_SilkS:continue
        r=box(g.GetBoundingBox(),.1)
        if any(overlap(r,box(pad.GetBoundingBox(),.15)) for ff in b.GetFootprints() for pad in ff.Pads()):
            g.SetLayer(k.F_Fab);moved+=1
k.SaveBoard(str(p),b)
Path('pcb/layout/silkscreen-review.json').write_text(json.dumps({'printedReferences':shown,'fabricationOnlyReferences':hidden,'graphicsMovedToFab':moved},indent=2))
print('Printed',len(shown),'Fabrication-only',len(hidden),'graphics moved',moved)