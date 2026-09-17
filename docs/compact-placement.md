# Compact placement candidate — not a release

User requirement: external microSD insertion/removal without opening enclosure;
compact battery-led outline, with real assembly and routing clearance.

## Current PCB candidate
- Outline 36 x 76 mm, KiCad X82..118, Y44..120, R3 corners; reduced from
  36 x 86 mm (11.6% area reduction). This is an intermediate compact candidate,
  NOT an established minimum or a battery-sized finished design.
- Battery basis: Adafruit 1578 product listing, 29 x 36 x 4.75 mm
  (https://www.adafruit.com/product/1578). Existing conservative project reserve
  is 30.1 x 36 x 6.1 mm, including 1 mm thickness allowance, not a verified
  swelling specification. Existing tray outer width 32.2 mm leaves 1.9 mm per
  side within a 36 mm PCB width; Z separation and lead routing remain unverified.
- J4 is at (88.6,61), KiCad rotation 90 degrees. Local card projection is -Y;
  after rotation, insertion/removal is along board -X. Socket mouth X82.9 mm;
  nominal inserted card tip X78.9 mm projects 3.1 mm beyond the PCB left edge.
  Source: Molex SD-104031-001 and installed matching KiCad footprint.
- Reserve the external approach at X<82 mm, Y54..68 mm, unobstructed by
  enclosure ribs, straps, connector cables or fasteners. Card center Y60.905 mm.
  Provide a finger recess: a narrow slot alone is insufficient for a push-pull
  connector. Final aperture Z/height and wall recess require mechanical fit work.
- U10/U11 moved into vacated SD region. XIAO and lower mounting holes moved
  up 10 mm. SD passives, IMU and standby control parts redistributed.
- Current board and all placements are saved. Before any regeneration reconcile
  source/base with pcb/backups/battery-compact/current-placement.json; no board
  regeneration was used in this pass. Original PCB and source are backed up.

## Executed validation
- Pad-by-pad net assignments identical to pre-edit board, 115 footprints retained.
- Visual review confirms SD faces left with projected card outside Edge.Cuts,
  no obstructing board components in the external approach; SW2 faces right.
- Placement envelope intersections: zero on final candidate.
- ERC passes (79 advice); DFM passes. DRC has 295 unrouted items and 295 warnings
  (166 silk-over-copper, 66 silk overlap, 35 library issues, 28 text-height).
  No courtyard-overlap, board-outline, or copper-clearance violations reported.
- Board remains unrouted; no manufacturing or enclosure-fit claim.

## Remaining work
The legacy compact-pendant generator still assumes lid-off SD service, deleted
D2/D3 indicators and legacy speaker geometry. Its current models are obsolete.
Do not fabricate them against this PCB. A complete enclosure revision must move
the bottom posts/USB opening, add the left SD finger recess and verify battery,
diffuser, component heights and wire paths. Further compaction must consider
two-sided assembly versus battery separation; this candidate retains top-side
assembly and all existing components rather than silently changing the stack.