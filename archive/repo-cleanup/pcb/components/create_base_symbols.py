"""Reproducible local symbols from documented exact pin tables; not footprint generation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def write_symbol(folder, filename, name, pins):
    lines = ['(kicad_symbol_lib (version 20231120) (generator "embedr")',
             f'(symbol "{name}" (in_bom yes) (on_board yes)',
             '(property "Reference" "U" (at 0 12.7 0) (effects (font (size 1.27 1.27))))',
             f'(property "Value" "{name}" (at 0 -12.7 0) (effects (font (size 1.27 1.27))))',
             f'(symbol "{name}_0_1" (rectangle (start -10.16 10.16) (end 10.16 -10.16) (stroke (width 0.254) (type default)) (fill (type background))))',
             f'(symbol "{name}_1_1"']
    for number, pin, kind, x, y, angle in pins:
        lines.append(f'(pin {kind} line (at {x} {y} {angle}) (length 2.54) '
                     f'(name "{pin}" (effects (font (size 1.0 1.0)))) '
                     f'(number "{number}" (effects (font (size 1.0 1.0)))))')
    lines.append(')))')
    (ROOT / folder / filename).write_text('\n'.join(lines) + '\n')

write_symbol('im69d130', 'IM69D130.kicad_sym', 'IM69D130', [
    (1,'DATA','output',12.7,0,180), (2,'VDD','power_in',-12.7,7.62,0),
    (3,'CLOCK','input',-12.7,2.54,0), (4,'SELECT','input',-12.7,-2.54,0),
    (5,'GND','power_in',-12.7,-7.62,0)])
write_symbol('dm3d-sf', 'DM3D-SF.kicad_sym', 'DM3D_SF', [
    (1,'DAT2','bidirectional',12.7,7.62,180), (2,'DAT3_CS','bidirectional',-12.7,5.08,0),
    (3,'CMD_MOSI','input',-12.7,2.54,0), (4,'VDD','power_in',-12.7,7.62,0),
    (5,'CLK','input',-12.7,0,0), (6,'VSS','power_in',-12.7,-7.62,0),
    (7,'DAT0_MISO','bidirectional',12.7,2.54,180), (8,'DAT1','bidirectional',12.7,5.08,180),
    (9,'DETECT_A','passive',12.7,-2.54,180), (10,'DETECT_B','passive',12.7,-5.08,180),
    (11,'SHIELD','passive',12.7,-7.62,180)])