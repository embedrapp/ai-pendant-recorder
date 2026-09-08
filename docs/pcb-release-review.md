# PCB/enclosure reconciliation — release blocked

Requirements: 32 x 76 mm enclosure exterior, rectangular elongated carrier,
two copper layers, 1.62 mm current PCB thickness, all components on front,
no underside components over the LiPo tray. Initial 27 x 67 mm target, now
28 x 70 mm chamfered board centered
at KiCad (100,100), CAD X=KiCad X-100, CAD Y=100-KiCad Y.
Mount centers CAD (+/-12,+/-32), 2.2 mm NPTH, subject to edge/fastener review.
Fabrication target: ordinary FR4 two-layer prototype, no order approval implied.

Initial evidence: six footprints, no outline, no copper; original fingerprint
8005c5678a30f30112cf4cf8ed2af8cf5f10719aa639c57425e5a48e7c8ea25c.
All existing locks are inherited draft state, not evidence of placement acceptance.

Electrical findings: I2S BCLK currently uses D8/GPIO7, also microSD SCK;
move BCLK to unused D3/GPIO4. EN is a reset INPUT, not amplifier GPIO control;
disconnect amplifier shutdown from module EN. Resolve low-battery SD_MODE
absolute maximum and power-off behavior before release. Speaker, cell,
connectors, switches and antenna envelopes must be selected/verified.
XIAO record peak camera current is ~366 mA before amplifier load: a 0.3 A
slide switch is NOT approved as a direct whole-device battery disconnect.

Mechanical findings: camera/mic coordinates in enclosure are placeholders,
USB mating plane is unverified, module wrapper says approximately 15 mm stack
while enclosure assumes 10 mm. Do not claim exact fit until reconciled.
Source: Seeed filesystem wiki confirms GPIO7/8/9 used by SD SPI, but contradicts
itself on CS (GPIO3 vs GPIO21); resolve from exact board revision schematic.

Acceptance: source build/netlist, electrical review, actual outline/holes,
whole-board placement review, route/return-path review, fresh ERC/DRC/PDK DFM,
STEP fit/interference review, exact BOM and same-revision verified fabrication
exports. Fit, skin temperature, RF, audio and battery safety require prototype tests.

## Current implementation and checks

Added J1 battery and J2 speaker JST B2B-PH-K-S connectors (pin 1 positive,
pin 2 negative), SW1 PTS645SM43SMTR92 LFS record button, SW2 JS202011AQN
standby switch, R3 2 kohm SD_MODE series resistor, four M2 2.2 mm NPTHs.
R3 is grounded in MAX98357 datasheet chunk 0042, which recommends ~2 kohm
when the 3.3 V control supply can exceed amplifier VDD. D3/GPIO4 is now
BCLK; D4/GPIO5 drives AMP_ENABLE through R3. The module EN has its own net.
SW2 grounds MCU_EN and AMP_SD in standby. Battery and charger remain connected;
this is NOT the true battery isolation circuit required for final release.

Latest source build passes (15 components); netlist and repeated board screenshots
inspected. Current physical outline is 28 x 70 mm with 1.2 mm corner chamfers,
center (100,100), four mounting holes at (88,68), (112,68), (88,132), (112,132).
The holes match the existing enclosure XY standoff centers. Actual drill-to-side
distance is 0.9 mm; 4.3 mm courtyard rings extend 0.15 mm beyond the board and
are NOT drilled holes. Fastener bearing strength remains unqualified.

Latest checks 2026-09-07T12:16:24Z:
- ERC: pass, 0 errors/warnings, 41 style advice.
- DRC: FAIL, 33 unconnected errors, 30 warnings (silk and R1 library mismatch).
- PDK DFM: 10 rules passed, 5 skipped, no findings. This does not qualify an
  unrouted board for fabrication. `canOrder=false`.
- No routing or fabrication exports performed. No source-only success is a fit pass.

Placement metadata helper rejected positions because it could not resolve footprints
and generated extraneous inferred IDs. Nothing from that rejected operation was
applied. Exact runtime IDs and actual board coordinates were instead persisted with
a focused source patch, which passed evaluation. Regeneration behavior still requires
comparison; retain the current physical board rather than regenerating as a refresh.

## Remaining blockers (do not order)

- Exact module stack/lens/mic metrology is unavailable; the existing 13 mm front Z
  is NOT established as sufficient for the approximate 15 mm assembly height.
- SW1 is now top-actuated at CAD (-1,+6), but enclosure still has a SIDE button
  opening. It requires a qualified front plunger/opening or an exact side switch.
- J2 through-hole tails project into the nominal under-board cell region. Move the
  connector or change to a verified low-profile SMT mating system; no solder point
  may contact the cell. J1 and the speaker retaining ring also need a 3D fit review.
- Selected PH header supports 0.8–1.6 mm board thickness per record; current board
  says 1.62 mm. Resolve nominal stackup and connector tolerance before release.
- Cell and speaker MPNs unresolved. Equal J1/J2 housings permit dangerous cross-mating;
  use different keyed systems or a captive assembly with documented safeguards.
- U1 USB graphic intentionally faces the top, but actual mating face is not verified
  against the shell opening. SW2 side actuator reach is similarly unverified.
- Need antenna/coax keepout, hard power isolation, test points, supply/current budget,
  exact passive ratings/MPNs, assembly access, silk cleanup and routed return paths.
- Enclosure revision ec844702 remains the earlier concept; it was NOT rebuilt or
  validated against this new PCB context. Its old no-outline statements are historical.

Original board preserved at `pcb/backups/pre-enclosure-fit.kicad_pcb`; this backup is
the six-component UNROUTED input, not a manufacturing-ready recovery image.