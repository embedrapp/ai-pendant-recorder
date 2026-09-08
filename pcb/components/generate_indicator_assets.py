"""Private datasheet-derived symbols and lands. See docs/rgb-haptics.md."""
from pathlib import Path
root=Path(__file__).parent
def symbol(folder,name,pins):
    p=root/folder; p.mkdir(exist_ok=True)
    n=(len(pins)+1)//2
    s=f'(kicad_symbol_lib (version 20211014) (generator embedr) (symbol "{name}" (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 {n*1.27+3} 0) (effects (font (size 1.27 1.27)))) (property "Value" "{name}" (at 0 {n*1.27+1} 0) (effects (font (size 1.27 1.27)))) (symbol "{name}_0_1" (rectangle (start -10.16 {n*1.27}) (end 10.16 {-n*1.27}) (stroke (width 0.254) (type default)) (fill (type background)))) (symbol "{name}_1_1"'
    for i,(num,label,kind) in enumerate(pins):
        x,a=(-12.7,0) if i<n else (12.7,180)
        y=(n-1)*1.27-(i%n)*2.54
        s+=f'(pin {kind} line (at {x} {y} {a}) (length 2.54) (name "{label}" (effects (font (size 1 1)))) (number "{num}" (effects (font (size 1 1)))))'
    (p/(name+'.kicad_sym')).write_text(s+')))')
def footprint(folder,name,lands,bx,by):
    s=f'(footprint "{name}" (version 20221018) (generator embedr) (layer "F.Cu") (attr smd) (fp_text reference "REF**" (at 0 {-by-1}) (layer "F.SilkS") (effects (font (size .6 .6) (thickness .1)))) (fp_text value "{name}" (at 0 {by+1}) (layer "F.Fab") (effects (font (size .6 .6) (thickness .1))))'
    for layer,x,y in [('F.Fab',bx,by),('F.CrtYd',max(bx,max(abs(l[1])+l[3]/2 for l in lands))+.25,max(by,max(abs(l[2])+l[4]/2 for l in lands))+.25)]:
        s+=f'(fp_rect (start {-x} {-y}) (end {x} {y}) (stroke (width .05) (type solid)) (fill none) (layer "{layer}"))'
    for num,x,y,w,h in lands:
        s+=f'(pad "{num}" smd rect (at {x} {y}) (size {w} {h}) (layers "F.Cu" "F.Mask" "F.Paste"))'
    (root/folder/(name+'.kicad_mod')).write_text(s+')')
symbol('rgb','APGF0607',[(1,'A','passive'),(2,'G','passive'),(3,'B','passive'),(4,'R','passive')])
footprint('rgb','APGF0607',[(1,-.2,-.2,.25,.25),(2,-.2,.2,.25,.25),(3,.2,.2,.25,.25),(4,.2,-.2,.25,.25)],.325,.325)
symbol('motor-ldo','AP2112K_3V3',[(1,'VIN','power_in'),(2,'GND','power_in'),(3,'EN','input'),(4,'NC','no_connect'),(5,'VOUT','power_out')])
footprint('motor-ldo','AP2112K_3V3',[(1,-1.2,-.95,.8,.55),(2,-1.2,0,.8,.55),(3,-1.2,.95,.8,.55),(4,1.2,.95,.8,.55),(5,1.2,-.95,.8,.55)],.8,1.5)
symbol('motor-diode','NSVR0320',[(1,'K','passive'),(2,'A','passive')])
footprint('motor-diode','NSVR0320',[(1,-1.115,0,.63,.83),(2,1.115,0,.63,.83)],.85,.625)
pins=[(i+1,'A'+str(i),'input') for i in range(5)]
pins += [(i+6,'LED'+str(i),'output') for i in range(8)]
pins += [(14,'VSS','power_in')]+[(i+7,'LED'+str(i),'output') for i in range(8,16)]
pins += [(23,'OE','input'),(24,'A5','input'),(25,'EXTCLK','input'),(26,'SCL','input'),(27,'SDA','bidirectional'),(28,'VDD','power_in')]
symbol('pca9685pw','PCA9685PW_corrected',pins)