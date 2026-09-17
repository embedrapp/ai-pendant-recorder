# Compact mechanical/placement revision

Candidate carrier: 44 × 60 mm R3, two copper layers, top-side components.
Shell target: 50 × 70 mm excluding loop, full 15 mm Sense stack above PCB,
protected 603450 battery behind PCB in a removable tray. No claim of minimum
possible size: battery, connector access and full Sense assembly dominate.
Bottom-facing USB-C: U1 rotated 180 degrees. Mount holes at ±19/±27 mm.
Rear battery clearance keeps solder tails away from the pouch; no compressive
retention. Upper side antenna zone and detachable front/shutter modules.
Material assumption: PETG, 0.4 mm nozzle, 0.2 mm layers; trial-fit gap 0.3 mm.
Exact purchased battery PCM/lead exit, motor identity, antenna and optical port
datums remain measurement gates. Existing board/CAD retained under backups/archive.

## Current evidence / unfinished acceptance

All 43 footprints synchronized and manually positioned on the 44×60 R3 carrier.
Inspection reports zero same-side rendered-envelope intersections. U1's USB/body
graphic intentionally extends 0.547 mm past the bottom; its solder pads remain
inside. Rounded Edge.Cuts are not supported by the placement containment checker,
so its unknown findings are NOT a containment pass. Board screenshot reviewed;
central silkscreen remains crowded. No copper routing performed (107 airwires).
Source comments persisted from the inspected coordinates after the placement-comment
tool failed footprint resolution; LSP lint timed out, evaluator passed.

Fresh ERC passed with 70 naming advice. DRC: 107 unconnected findings plus eight
0.15 mm RGB pad gaps below the board's 0.16 mm rule, and 38 warnings. Do not
blindly enlarge these tiny manufacturer lands or lower global clearance; review
an appropriate fabrication profile and scoped same-package rule before routing.
No placement freeze, manufacturing approval or all-component fit acceptance yet.

Enclosure source `mechanical/compact-pendant.py`, active `pendant.cad.json`.
Cloud revision `rev-699a1b13bb7f50bbd056d08ae395d6df121b9782dba1ac015158a79c486cc6ac`
contains nine inspectable solids; exported to
`mechanical/exports/compact-pendant-fit-prototype.step`.
Shell body 50×70×33 mm; total modeled bounds 51×76.5×39.5 mm including loop,
backer, shutter and light inserts. Only valid-solid checks passed, NOT interference.
The exact electronic STEP components are not assembled into this revision.
Optical/USB/SD datums, antenna size/bend relief, plunger detail, shutter full-open
travel/frame attachment, magnet retention, tray retention and print orientation
still need refinement. Legacy individual-part manifests still point at old CAD;
use only the active pendant design for this candidate. This is a fit prototype,
not a completed enclosure or print-ready set.