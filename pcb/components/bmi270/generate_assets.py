"""Reproducible exact BMI270 assets; dimensions and provenance in README.md."""
from pathlib import Path
p = Path(__file__).parent
pins = ['SDO','ASDx','ASCx','INT1','VDDIO','GNDIO','GND','VDD','INT2','OCSB','OSDO','CSB','SCx','SDx']
s = '(kicad_symbol_lib (version 20211014) (generator embedr)\n (symbol "BMI270" (in_bom yes) (on_board yes)\n'
for name, value, y in [('Reference','U',12.7),('Value','BMI270',10.16)]:
    s += f'(property "{name}" "{value}" (at 0 {y} 0) (effects (font (size 1.27 1.27))))\n'
s += '(symbol "BMI270_0_1" (rectangle (start -7.62 8.89) (end 7.62 -8.89) (stroke (width 0.254) (type default)) (fill (type background))))\n(symbol "BMI270_1_1"\n'
for i, name in enumerate(pins):
    left = i < 7
    x, angle = (-10.16, 0) if left else (10.16, 180)
    y = 7.62 - (i % 7)*2.54
    kind = 'power_in' if name in ['VDD','VDDIO','GND','GNDIO'] else 'bidirectional' if name in ['SDO','ASDx','ASCx','INT1','INT2','SDx'] else 'output' if name == 'OSDO' else 'input'
    s += f'(pin {kind} line (at {x} {y} {angle}) (length 2.54) (name "{name}" (effects (font (size 1 1)))) (number "{i+1}" (effects (font (size 1 1)))))\n'
(p/'BMI270.kicad_sym').write_text(s+')))\n')
f = '(footprint "BMI270" (version 20221018) (generator embedr) (layer "F.Cu") (attr smd)\n'
f += '(fp_text reference "U" (at 0 -2.1) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))\n'
f += '(fp_text value "BMI270" (at 0 2.1) (layer "F.Fab") (effects (font (size 0.8 0.8) (thickness 0.12))))\n'
for layer, x, y in [('F.Fab',1.5,1.25),('F.CrtYd',1.75,1.5)]:
    f += f'(fp_rect (start {-x} {-y}) (end {x} {y}) (stroke (width 0.05) (type solid)) (fill none) (layer "{layer}"))\n'
f += '(fp_circle (center -1.6 -1.45) (end -1.5 -1.45) (stroke (width 0.1) (type solid)) (fill none) (layer "F.SilkS"))\n'
lands = [(-1.1625,y,.475,.25) for y in [-.75,-.25,.25,.75]]
lands += [(x,.9125,.25,.475) for x in [-.5,0,.5]]
lands += [(1.1625,y,.475,.25) for y in [.75,.25,-.25,-.75]]
lands += [(x,-.9125,.25,.475) for x in [.5,0,-.5]]
for i,(x,y,w,h) in enumerate(lands,1):
    f += f'(pad "{i}" smd rect (at {x} {y}) (size {w} {h}) (layers "F.Cu" "F.Paste" "F.Mask"))\n'
(p/'BMI270.kicad_mod').write_text(f+')\n')