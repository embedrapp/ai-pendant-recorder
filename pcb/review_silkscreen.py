"""Target only reported silk collisions; retain body graphics on fabrication layer."""
import json
import shutil
from pathlib import Path
import pcbnew as k

p = Path(__file__).parent / 'layout/layout.kicad_pcb'
report = json.loads((p.parent / '.embedr-board/manufacturing-readiness.json').read_text())
b = k.LoadBoard(str(p))
backup = p.with_suffix('.kicad_pcb.pre-silk-review.bak')
if backup.exists():
    assert backup.read_bytes() == p.read_bytes(), 'Existing backup differs; inspect before retry'
else:
    shutil.copy2(p, backup)
ids = set()
for d in report['checks']['drc']['details']:
    if d.get('type') in ('silk_over_copper', 'silk_edge_clearance', 'silk_overlap'):
        for i in d['items']:
            if 'on F.Silkscreen' in i['description']:
                ids.add(i['uuid'])
for f in b.GetFootprints():
    for g in f.GraphicalItems():
        if g.m_Uuid.AsString() in ids and g.GetLayer() == k.F_SilkS:
            g.SetLayer(k.F_Fab)
    # Agent-chosen legible reference locations, away from pads and board edges.
    positions = {'H1': (88.2,72), 'H2': (111.8,72), 'H3':(88.2,128),
                 'H4':(111.8,128), 'U1':(100,88.5), 'U2':(100,92),
                 'C1':(104,99), 'C2':(99,102), 'R1':(106,89),
                 'R2':(94.5,99), 'R3':(94.5,96), 'J2':(102.5,109),
                 'SW1':(109,94), 'SW2':(107,109.5), 'J1':(100,133)}
    x,y = positions[f.GetReference()]
    r = f.Reference()
    r.SetPosition(k.VECTOR2I(k.FromMM(x),k.FromMM(y)))
    r.SetTextAngle(k.EDA_ANGLE(0,k.DEGREES_T))
    r.SetTextSize(k.VECTOR2I(k.FromMM(.8),k.FromMM(.8)))
    r.SetTextThickness(k.FromMM(.12))
k.SaveBoard(str(p),b)
print('Silk-only cleanup; original graphics retained on F.Fab. Backup:',backup)