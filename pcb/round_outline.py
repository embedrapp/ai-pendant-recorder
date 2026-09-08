"""Replace only the eight chamfered outline edges with a 2 mm radius outline.
Run with KiCad Python. Refuses routed input; preserves all footprints and nets.
"""
from pathlib import Path
import shutil
import math
import pcbnew as k

p = Path(__file__).parent / 'layout/layout.kicad_pcb'
b = k.LoadBoard(str(p))
assert len(b.GetTracks()) == 0, 'Review routed copper before outline edits'
edges = [d for d in b.GetDrawings() if d.GetLayer() == k.Edge_Cuts]
assert len(edges) == 8, 'Unexpected outline; inspect first'
backup = p.with_suffix('.kicad_pcb.pre-rounded-outline.bak')
assert not backup.exists(), 'Backup exists; do not overwrite'
shutil.copy2(p, backup)
for e in edges:
    b.Remove(e)

def pt(x, y):
    return k.VECTOR2I(k.FromMM(x), k.FromMM(y))

for a, z in [((88,65),(112,65)), ((114,67),(114,133)),
             ((112,135),(88,135)), ((86,133),(86,67))]:
    s=k.PCB_SHAPE(); s.SetShape(k.SHAPE_T_SEGMENT)
    s.SetStart(pt(*a)); s.SetEnd(pt(*z)); s.SetLayer(k.Edge_Cuts)
    s.SetWidth(k.FromMM(.05)); b.Add(s)
q=2/math.sqrt(2)
for a,m,z in [((112,65),(112+q,67-q),(114,67)),
              ((114,133),(112+q,133+q),(112,135)),
              ((88,135),(88-q,133+q),(86,133)),
              ((86,67),(88-q,67-q),(88,65))]:
    s=k.PCB_SHAPE(); s.SetShape(k.SHAPE_T_ARC)
    s.SetArcGeometry(pt(*a),pt(*m),pt(*z)); s.SetLayer(k.Edge_Cuts)
    s.SetWidth(k.FromMM(.05)); b.Add(s)
k.SaveBoard(str(p),b)
print('Retained 28 x 70 mm bounds; four tangent R2 corners; backup:',backup)