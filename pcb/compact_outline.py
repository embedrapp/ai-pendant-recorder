"""Replace only root Edge.Cuts; preserve footprints and copper. mm, 36 x 86 R3."""
from pathlib import Path
import re, math, uuid
p=Path(__file__).parent/'layout/layout.kicad_pcb'
s=p.read_text()
# Balanced root forms, respecting quoted strings.
depth=0; quoted=False; escape=False; start=0; forms=[]
for i,c in enumerate(s):
    if quoted:
        if escape: escape=False
        elif c=='\\': escape=True
        elif c=='"': quoted=False
        continue
    if c=='"': quoted=True
    elif c=='(':
        depth+=1
        if depth==2: start=i
    elif c==')':
        if depth==2: forms.append((start,i+1))
        depth-=1
for a,b in reversed(forms):
    f=s[a:b]
    if re.match(r'\(gr_(line|arc|rect|poly)',f) and '(layer "Edge.Cuts")' in f:
        s=s[:a]+s[b:]
items=[]
def line(a,b):
    items.append(f'(gr_line (start {a[0]} {a[1]}) (end {b[0]} {b[1]}) (stroke (width 0.05) (type default)) (layer "Edge.Cuts") (uuid "{uuid.uuid4()}"))')
def arc(a,m,b):
    items.append(f'(gr_arc (start {a[0]} {a[1]}) (mid {m[0]} {m[1]}) (end {b[0]} {b[1]}) (stroke (width 0.05) (type default)) (layer "Edge.Cuts") (uuid "{uuid.uuid4()}"))')
k=3/math.sqrt(2)
line((85,44),(115,44));arc((115,44),(115+k,47-k),(118,47))
line((118,47),(118,127));arc((118,127),(115+k,127+k),(115,130))
line((115,130),(85,130));arc((85,130),(85-k,127+k),(82,127))
line((82,127),(82,47));arc((82,47),(85-k,47-k),(85,44))
pos=s.rfind(')');p.write_text(s[:pos]+'\n'+'\n'.join(items)+'\n'+s[pos:])