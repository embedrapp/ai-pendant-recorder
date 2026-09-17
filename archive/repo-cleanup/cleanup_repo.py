"""Archive obsolete electronics/docs without deleting routed or mechanical work."""
from pathlib import Path
import re, shutil, json
r=Path(__file__).resolve().parents[1]
a=r/'archive/repo-cleanup'
a.mkdir(parents=True,exist_ok=True)
moves=[]
def move(p):
    dest=a/p.relative_to(r)
    if dest.exists(): raise RuntimeError('Archive collision: '+str(dest))
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.move(p,dest)
    moves.append([str(p.relative_to(r)),str(dest.relative_to(r))])
# Derive active local package roots from both retained electrical entrypoints.
active=set()
for entry in ['ai_pendant_recorder.zen','pts841-fixture.zen']:
    for name in re.findall(r'Module\("\./components/([^/]+)/', (r/'pcb'/entry).read_text()): active.add(name)
# Check retained wrappers do not reach into another local package.
for name in list(active):
    for p in (r/'pcb/components'/name).rglob('*.zen'):
        for target in re.findall(r'Module\("([^"@]+)"\)',p.read_text()):
            q=(p.parent/target).resolve()
            try: active.add(q.relative_to(r/'pcb/components').parts[0])
            except ValueError: pass
for p in list((r/'pcb/components').iterdir()):
    if p.is_dir() and p.name not in active: move(p)
    elif p.is_file() and p.suffix=='.py': move(p)
# Historical executable board mutations must not look like current workflows.
for p in list((r/'pcb').glob('*.py')): move(p)
for p in list((r/'docs').glob('*.md')):
    if p.name not in ['bom.md','rgb-matrix.md']: move(p)
for p in [r/'docs/update_base_bom.py',r/'docs/silkscreen-warning-disposition.json']:
    if p.exists(): move(p)
# Retain historical archives and all CAD/board artifacts in place.
for p in [r/'pcb/README.md',r/'docs/datasheets/README.md']:
    if p.exists(): move(p)
p=r/'pcb/pcb.toml'; original=p.read_text(); (a/'pcb/pcb.toml').write_text(original)
lines=[]
for line in original.splitlines():
    m=re.search(r'/components/([^"/]+)"\s*=',line)
    if not m or m.group(1) in active: lines.append(line)
p.write_text('\n'.join(lines)+'\n')
(a/'moves.json').write_text(json.dumps(moves,indent=2))
print('Active component packages:',sorted(active)); print('Archived paths:',len(moves))