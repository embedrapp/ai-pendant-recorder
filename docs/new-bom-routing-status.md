# New BOM integration / routing — placement frozen, ready for routing

## Route-readiness revision 220f3ac0

- Closed 28 x 70 mm two-layer outline retained. All 15 footprints are on the
  front, inside by anchor, and locked against accidental routing-time movement.
- M2 NPTH centers moved to X=88.2/111.8, Y=68.5/131.5. Their rendered
  envelopes now fit inside Edge.Cuts; mechanical generator must use the same
  board-derived centers on its next build.
- U2 amplifier moved to (100,96); its 100 nF and 10 uF bypass capacitors and
  SD-mode resistors are grouped locally. J2 speaker connector is immediately
  below the amplifier. R1 is between the XIAO and side record switch.
- SW1 is intentionally edge-actuated at (112,94), rotation 90; its copper pads
  are inside and only the actuator/courtyard crosses the right Edge.Cuts.
  SW2 similarly has an intentional right-edge actuator overhang. U1 remains at
  the top edge for USB access and Sense-board volume.
- J2 mechanical anchors now have distinct MP1/MP2 pad/net attribution. They
  remain electrically isolated from each other and ground. Fresh PDK DFM now
  passes instead of aborting on unattributed copper.
- Primary source build and exact netlist inspection pass. Fresh ERC has zero
  errors/warnings (41 style advice). Fresh DRC has 33 missing-connection errors,
  exactly the expected unrouted state, plus 30 pre-routing silkscreen/library
  warnings. There are zero tracks, vias, or zones.
- Full F.Cu/F.Fab/Edge.Cuts capture was reviewed: no footprint intersection,
  all electrical pads are inboard, and the two intentional right-edge controls
  remain accessible. This is ready to enter routing, not fab-ready.

Routing constraints: retain two layers; preserve all 15 placements; treat the
four NPTH mounting holes as obstacles; use wider copper for VBAT, GND, SPK_P
and SPK_N than logic; keep the BTL speaker pair together and neither output to
ground; route I2S directly without unnecessary vias; retain a continuous ground
return and keep antenna/coax, microphone inlet, USB, and control-access volumes
free. After routing, review F.Cu and B.Cu separately, correct silkscreen, then
rerun ERC/DRC/DFM. The enclosure still requires a fresh board-context rebuild
and physical prototype fit validation; those do not block creating the routing
candidate but do block fabrication release.

## Uploaded-datasheet integration checkpoint

The PTS841 download blocker is resolved. Uploaded document
`ds_6387b39722da309d0fd7` was searched and its complete page 2 and
numbered top-view drawing reviewed. Original PDF retained at
`docs/datasheets/pts841.pdf`.

- Created private PTS841GKSMTR LFS symbol/footprint/package: four numbered
  terminals, common pairs 1–2 and 3–4, no optional pegs or ESD terminal.
- Created private JST BM02B-SRSS-TB(LF)(SN) package from the retained
  upstream KiCad footprint and manufacturer SH drawings. Mechanical tabs
  are unnumbered, electrically floating solder anchors.
- Built both in `pcb/pts841-fixture.zen`; rendered the switch symbol and
  fixture footprints. Integrated SW1 and J2 in the primary source and
  synchronized the board without removing its outline or other parts.
- SW1: (112,94), 90 degrees, actuator toward right edge; pads remain
  inside, nominal actuator projects 0.15 mm beyond edge. Enclosure opening
  remains to be reconciled. J2: (104,102), 0 degrees; pin 1 SPK_P,
  pin 2 SPK_N. Different SH/PH interfaces prevent speaker/battery mating.
- Backup of pre-integration source and physical board/project retained at
  `pcb/backups/pre-pts841-integration/`.
- Primary source build passes (15 components). Fresh ERC: zero errors or
  warnings. Fresh DRC: 33 unconnected-item errors, 30 warnings, five ignored
  checks. No copper was added; routing is NOT completed.
- Latest DFM is unavailable: IPC-2581 rejects unattributed functional
  F.Cu copper. Investigate unnumbered connector mounting tabs/export handling;
  do not assign them a fabricated electrical purpose just to pass a checker.

Remaining before routing acceptance: reconcile larger battery tray, speaker
seat, switch access, connector tails, actual module/microphone/antenna
envelopes and mounting clearances; finish placement review and silkscreen
cleanup; establish routing rules/keepouts, route, review both copper layers,
and rerun checks. Mechanical source and firmware were not changed in this
checkpoint. The historical evidence below predates this integration.

## Authorized scope and retained constraints

User authorized design and PCB placement changes through completed routing.
Use `pendant-parts-selection.md`: protected LP502540 500 mAh cell,
CMS-16093-078L100 wired 8-ohm / 0.7 W speaker, PTS841GKSMTR LFS side
record switch, BM02B-SRSS-TB(LF)(SN) speaker header and documented harnesses.
Retain XIAO 113991115, MAX98357AETE+T and low-current JS202011AQN standby.
Keep two copper layers, front-side assembly, 32 x 76 mm enclosure plan envelope,
and existing 28 x 70 mm board unless mechanical reconciliation requires revision.
Nominal cell voltage is 3.7 V; finished-pack dimensions and permissible load
current remain supplier-dependent. Standby does not provide battery isolation.
Target is a prototype, not an approved manufacturing release.

## Current evidence

- Inspected source, parts shortlist, prior release review, board outline, exact
  placement and pad nets; captured the current board.
- Board fingerprint: `5216797bb57bbe7a78afd967205fa1b0b05646915bb02d6fcb17fc72dd5ab889`.
- 15 footprints, closed outline, 0 tracks, 0 vias, 0 zones; capture reports
  33 unrouted airwires. No new build, ERC, DRC or DFM performed this pass.
- Exact replacement switch and speaker header searches returned no library records.
- JST manufacturer SH PDF retained in `docs/datasheets/jst-sh.pdf`, from
  https://www.jst-mfg.com/product/pdf/eng/eSH.pdf . Privately indexed as
  `ea3071ca5ee5a6069eba534fa39a10f34c9fb742ee42135a69ab4156bfa0f5de`.
- Upstream KiCad BM02B-SRSS-TB footprint downloaded into `docs/datasheets/`
  for comparison only; NOT installed or validated against the drawing yet.
- PTS841 manufacturer PDF direct retrieval/indexing returned HTTP 403.
  Distributor attempts returned HTTP 403 or transport failures. Manufacturer
  text extraction confirms SPST-NO, 50 mA / 12 V, 1.25 mm nominal height,
  0.2 +/-0.1 mm travel; GK has no pegs or ESD pin. Flattened drawing text
  is insufficient to establish exact pad positions and circuit mapping.
- Legacy ckswitches PDF URL redirected to HTML, retained explicitly as
  `pts841-redirect.html`, not usable as a datasheet.

No electrical source, BOM, physical board, enclosure or firmware was changed.
No routing run was submitted. Existing design is preserved, not new-BOM compliant.

## Required next steps

1. Obtain readable PTS841GKSMTR LFS manufacturer drawing PDF (upload is sufficient).
   Inspect its circuit and land pattern images; author and validate an exact private
   package, not a PTS645 or generic-switch footprint substitute.
2. Compare JST drawing with upstream footprint (pad mapping, hold-downs, body,
   pin-one and mating envelope); validate a private connector package.
3. Preserve current source/board revision before replacing SW1 and J2. Sync and
   build, then inspect netlist and synchronize the board without losing its outline.
4. Reconcile side plunger and speaker harness access; move battery connector and
   through-hole standby tails outside the cell envelope or provide verified clearance.
   Resolve PCB 1.62 mm versus PH 1.6 mm nominal stackup. Reconcile battery tray,
   speaker seat and rear depth with drawing tolerances before claiming enclosure fit.
5. Review whole-board geometry and decoupler supply/ground loops, screw envelopes,
   USB access and antenna/coax constraints. Capture corrected placement and run
   fresh checks; disposition all non-routing findings explicitly.
6. Establish power/speaker trace widths and return paths from current and stackup
   assumptions. Request paid routing approval; verify original NPTH/keepout geometry
   survives conversion. Route on F.Cu/B.Cu, inspect both layers and run fresh
   ERC/DRC/DFM. Do not accept only a zero-airwire result.

Battery pulse capability, charge behavior, speaker output ceiling, exact module
stack fit, fastener qualification and thermal/RF/acoustic tests remain release gates.