"""Drawing-based external envelopes; not supplier-certified internal geometry."""
import json
import os
from build123d import Box, Cylinder, Pos, Compound


def gen_step():
    with open(os.environ['EMBEDR_MECHANICAL_PARAMETERS'], encoding='utf-8') as f:
        p = json.load(f)
    kind = p['component']
    if kind == 'battery':
        # Retained LiPol drawing nominal dimensions only. No invented NOVA PCM.
        body = Pos(0, 0, 3) * Box(34, 50, 6)
        body.label = 'BAT1 provisional cell envelope — PCM and leads unresolved'
        parts = [body]
    elif kind == 'motor':
        body = Pos(0, 0, 1.35) * Cylinder(5, 2.7)
        body.label = 'QX-1027 reference can — not verified Robu identity'
        tape = Pos(0, 0, -0.075) * Cylinder(5, 0.15)
        tape.label = 'Drawing adhesive tape 0.15 mm'
        # Wire exit coordinates/diameters are not dimensioned; omit rather than
        # fabricate a fit claim. Reserve a separate harness sweep in enclosure.
        parts = [body, tape]
    else:
        # PTS841 GK: no pegs or optional ESD contact. Nominal body envelope only;
        # actuator and lead solids require resolved drawing viewing orientation.
        body = Pos(0, 0, 0.625) * Box(3.6, 3.5, 1.25)
        body.label = 'PTS841GK body envelope — actuator and leads excluded'
        parts = [body]
    for part in parts:
        assert part.is_valid and part.volume > 0
    return Compound([solid for part in parts for solid in part.solids()])