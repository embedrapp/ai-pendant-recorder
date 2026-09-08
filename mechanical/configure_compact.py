"""Manifest migration only, no local CAD execution. Preserve stable parameter IDs."""
import json
from pathlib import Path
p=Path(__file__).parent/'pendant.cad.json'
m=json.loads(p.read_text());m['source']='mechanical/compact-pendant.py'
m['name']='Compact Sense pendant — modular fit prototype'
values={'width':50,'length':70,'wall':1.8,'floor_thickness':2,'front_z':20,'rear_z':13,
        'fit_gap':.3,'camera_x':0,'camera_y':-19,'camera_radius':4.5,'mic_x':6,'mic_y':-13,
        'explode':0}
for k,v in values.items():
    if k not in m['parameters']:m['parameters'][k]={'type':'number','label':k.replace('_',' '),'unit':'mm','step':.1}
    m['parameters'][k].update(value=v,min= v-2 if k not in ('camera_x','camera_y','mic_x','mic_y') else v-5,max=v+5)
m['description']='44x60 carrier; full Sense stack and 603450 battery. Modular printable fit prototype; optical ports and purchased component datums provisional.'
m['assumptions']=[{'id':'sense-height','label':'Sense stack above PCB','value':15,'unit':'mm','confidence':'datasheet','source':'Seeed retained assembly envelope'},
 {'id':'battery','label':'Cell nominal envelope','value':'34 x 50 x 6 mm; 1 mm expansion reserve','confidence':'assumed','source':'603450 generic reference, purchased NOVA PCM unknown'},
 {'id':'ports','label':'Optical/service datums','value':'Camera, microphone, SD and USB height provisional','confidence':'assumed','source':'Require exact assembled Sense metrology'},
 {'id':'process','label':'Print process','value':'PETG, 0.4 mm nozzle, 0.2 mm layer; 0.3 mm trial-fit gap','confidence':'assumed','source':'Fit prototype engineering choice'}]
m['checks']=[{'id':'valid-solids','label':'Valid solids','required':True}]
p.write_text(json.dumps(m,indent=2)+'\n')