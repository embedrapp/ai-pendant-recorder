"""Fix C1 label and redundant R1 pad rotations; no net/position/copper changes."""
from pathlib import Path
import shutil
import pcbnew as k
p=Path(__file__).parent/'layout/layout.kicad_pcb'
backup=p.with_suffix('.kicad_pcb.pre-silk-followup.bak')
assert not backup.exists()
shutil.copy2(p,backup)
b=k.LoadBoard(str(p))
for f in b.GetFootprints():
    if f.GetReference()=='C1':
        f.Reference().SetPosition(k.VECTOR2I(k.FromMM(105),k.FromMM(99)))
    if f.GetReference()=='R1':
        for pad in f.Pads():
            assert pad.GetOrientationDegrees()==270
            pad.SetOrientation(k.EDA_ANGLE(90,k.DEGREES_T))
k.SaveBoard(str(p),b)