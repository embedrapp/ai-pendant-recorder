"""Convert cloud tessellation to individual millimeter STL files; no CAD runtime."""
from pathlib import Path
import json, shutil, hashlib
import numpy as np
import trimesh

root=Path(__file__).resolve().parent
out=Path.home()/'Downloads'/'Pendant-36mm-Modular-Print-Kit'
out.mkdir(exist_ok=True)
scene=trimesh.load(root/'print-export/print-kit.glb')
mesh=scene.to_mesh()
# Cloud GLB is meter/Y-up; restore CAD millimeter/Z-up frame.
v=mesh.vertices.copy()*1000
mesh.vertices=np.column_stack((v[:,0],-v[:,2],v[:,1]))
centers=mesh.triangles_center
cells=np.rint(centers[:,:2]/100).astype(int)
ids=cells[:,0]+8*cells[:,1]
names=['rear-shell','lid','battery-tray','record-pusher','privacy-cap','speaker-retainer','clothing-backer','standby-slider','light-insert-D2','light-insert-D3','REFERENCE-PCB','REFERENCE-battery-nominal-34x50x6','REFERENCE-battery-reserved-34x50x7','REFERENCE-speaker-16.6x9.6x3.5','REFERENCE-motor-10x2.7']
# Same sorted reference order as the cloud generator.
refs=[f'C{i}' for i in range(1,9)]+['D1','D2','D3','J1','J2','J3','Q1']+[f'R{i}' for i in range(1,16) if i!=6]+['SW1','SW2']+[f'U{i}' for i in range(1,7)]
names += ['REFERENCE-'+ref+'-envelope' for ref in sorted(refs)]
assert len(names)==52 and set(ids)==set(range(52))
report=[]
for i,name in enumerate(names):
    part=mesh.submesh([np.flatnonzero(ids==i)],append=True)
    part.merge_vertices()
    part.remove_unreferenced_vertices()
    part.fix_normals()
    # Bed placement only, not an assertion of optimal support orientation.
    part.apply_translation([-part.bounds[:,0].mean(),-part.bounds[:,1].mean(),-part.bounds[0,2]])
    folder=out/('reference-dummies' if name.startswith('REFERENCE') else 'printable-parts')
    folder.mkdir(exist_ok=True)
    path=folder/(name+'.stl')
    part.export(path)
    check=trimesh.load(path,force='mesh')
    assert check.is_watertight and check.is_winding_consistent and check.volume>0, name
    report.append({'file':str(path.relative_to(out)),'dimensions_mm':check.extents.tolist(),'triangles':len(check.faces),'watertight':bool(check.is_watertight),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
shutil.copy2(root/'print-export/print-kit.step',out/'all-parts-master.step')
(out/'mesh-validation.json').write_text(json.dumps(report,indent=2))
print(out)
print('Verified',len(report),'individual watertight STL files')