# Compact redesign — active engineering checkpoint

## RGB/haptic integration — newest checkpoint

The previous missing-RGB/haptic statements below are historical. Both circuits
are now integrated; see [rgb-haptics.md](rgb-haptics.md) for exact mapping,
datasheet corrections and remaining engineering limits. Source builds with 43
components/65 nets. ERC passes with 0 errors, 0 warnings, 70 naming-only advice
entries (`style.redundant_name`). Pin/net renderer inspection confirms separate
LED resistor nets, regulated motor positive, low-side Q1 and flyback polarity.
Screenshot review still finds long crossings and crowded labels; 29 rendered
envelope overlaps remain, with zero body overlaps. This is not drawing-readability
or physical-assembly acceptance. Existing board remains untouched, stale and
unrouted (33 DRC missing connections, two warnings). Firmware unchanged by request.

## Latest schematic validation checkpoint (supersedes older checkpoints below)

- Integrated bare BMI270 U4 and separate C4/C5 100 nF bypass capacitors.
  Local symbol/14-land footprint follows Bosch DS000-08 pp135,137,143,145.
  Both supply pins connect to 3.3 V; both grounds to GND; CSB high; SDO low;
  auxiliary and interrupt pins NC. Physical footprint review remains open.
- Corrected MAX17048 CELL to protected BAT+ following the manufacturer p6
  instruction, despite its internally unconnected implementation. Updated BOM.
- Package sync and source build pass: 24 components, 39 nets. Renderer pin
  inspection shows U1 D4/U3 SDA/U4 SDx on FG_SDA, U1 D5/U3 SCL/U4 SCx on
  FG_SCL, R4/R5 supply ends on V3V3. The screenshot's apparently floating
  pull-up rail is not a source disconnection, but its presentation needs repair.
- Independent check reports ERC 0 errors/0 warnings, 49 advice entries, all
  `style.redundant_name`. These are naming advice, not electrical failures.
  Existing unsynchronized physical board reports 33 missing connections and
  two warnings; it is NOT the new schematic's validated physical implementation.
- Schematic screenshots now work. Visual review still finds crowded labels,
  unreadable passive values and long crossings; after one broad placement pass
  the renderer reports 15 envelope overlaps (zero component-body overlaps).
- RGB indicators/PWM driver and regulated haptics remain missing. PCA9685PW
  assets and AO3400A package were obtained for evaluation, not integrated or
  approved as compact final selections. AP2112 library metadata gives suspect
  EN/GND numbering and must be compared to manufacturer data before use.
- Firmware/board remain unchanged and incompatible with AMP_ENABLE on D2.
  This is partial progress, not completion or assembly approval.

This redesign supersedes the camera-free direction in historical status notes.
Retain the exact XIAO Sense camera/microphone/microSD stack, bottom USB-C,
onboard charger, bare MAX17048 and BMI270, two RGB indicators, physical controls,
speaker, motor, shutter, and reinforced external loop. Firmware is not being
silently reverted to the original generic DevKit target.

## Constraints and acceptance

- Battery checkpoint: the active tray now targets stocked Adafruit product 1578,
  a protected 1S 3.7 V 500 mAh pack with JST-PH. CAD reserves a conservative
  30.1 x 36.0 x 6.1 mm envelope (5.1 mm maximum documented body plus 1 mm
  expansion allowance). See `mechanical/front-battery-notes.md`. This supersedes
  the older 34 x 50 x 6 mm provisional tray statements below; purchase and
  electrical/thermal validation remain open.
- Compactness is a priority, but no final envelope is accepted yet. The selected
  battery body is approximately 30 x 36 x 5 mm; the old 26 × 42 mm tray cannot fit it.
- Start with two copper layers and top-side assembly; reconsider sides only with
  explicit battery, solder-tail, and module-stack clearance checks.
- Preserve the existing board before synchronization. Initial board SHA-256:
  `603e4063f2eb6049fc6aba0b6d4d31e2fab530e9a42179f2f1ad86a098743166`.
  Inspection found 15 footprints including four holes, no tracks/vias/zones,
  and screenshot reported 33 airwires. Existing locks are not placement approval.
- Keep an antenna wall zone and cable bend space clear of battery, copper,
  speaker/motor magnets, fasteners, and attachment hardware. Target 3–5 mm
  electronics clearance subject to assembled RF tests.
- Printed modules: rear shell, front shell, replaceable shutter and retainer,
  removable battery tray, speaker retainer, motor cradle, light-port inserts,
  optional clothing backer. Final process/tolerances remain to be validated.
- Acceptance requires source/netlist review, visual schematic review, placement
  geometry and images, ERC/DRC/DFM, current assembly STEP interference and service
  path checks, and printed/hardware validation. No release claim from a build.

## Findings to resolve before layout freeze

1. U3/U4, RGB LEDs, haptic circuit, J3 and new support parts are absent from Zen.
2. C1/C2 sourcing differs from the procurement BOM. R3 is amplifier-enable series
   resistance in the source, not an LED resistor. The price table counts four
   100 kΩ resistors for R1/R2/R8 although those references total three.
3. RGB channels require six current-limiting resistors and a GPIO/PWM budget;
   do not allocate camera, microphone or microSD pins to these functions.
   A shared-I2C PWM driver may be needed and would be a documented BOM addition.
4. QX-1027 is rated 2.5–3.5 V (datasheet p3), 85 mA running maximum and 230 mA
   starting/locked maximum at 3 V (p4). Direct 4.2 V BAT+ is not approved.
   Resolve a regulated motor supply and transient/current budget; PWM alone is
   not proof of voltage compatibility. D1 cathode must follow MOTOR+.
5. Superseded: the retained NOVA/LiPol three-wire drawing is no longer the active
   tray basis. Adafruit 1578 is the selected two-wire JST-PH protected candidate;
   delivered-pack polarity, PCM details, shipping and sample metrology remain gates.
6. The retained motor drawing is QX-1027-3.0-07, not proof of the Robu part.
   Model it as a reference variant, not a confirmed purchased component.
7. SW1 GK has neither pegs nor the ESD pin. Use the exact variant in its model.
8. Seeed retained datasheet p6 gives 21 × 17.8 × 15 mm with expansion board;
   the existing enclosure's assumed 10 mm stack is not accepted for this redesign.

## Local reference provenance

- PTS841 PDF SHA-256: `7c9c6ab89d64f98dcc287a2646c8fdceb7bc00973e170807c5de820f69a716bf`, p2.
- LiPol PDF SHA-256: `46d1f33d6de0c5ff81b80471a1f5973744574150349fc1152e5967f51f017052`, p1.
- QX motor PDF SHA-256: `636a2f1f12dba6d8a8be3817c067e20b3dcb9d23b5924e11af8e5077d5cb5a22`, pp3–4,9.

Status: inspection/reconciliation in progress; final assembly is not validated.

## Implemented checkpoint

### Schematic update checkpoint

Added U3 MAX17048 polling circuit, C3 bypass, R4/R5 shared 3.3 V I2C pull-ups,
and TP3/TP4. D4/D5 now carry I2C; AMP_ENABLE moved to D2. Existing firmware
and physical board are NOT synchronized to that pin change and must not be used
as a matched revision. Camera/microphone/microSD remain internal to U1.

Sync and root build passed with 21 components; netlist inventory inspected.
U3 uses the materialized library footprint provisionally: its description cites
an ST DFN package, so comparison with ADI land pattern 90-0065 is a release gate.
The datasheet pin table calls CELL internally unconnected but also says connect
to battery; this draft retains the BOM's NC choice pending reconciliation.

Saved agent-chosen positions for all 21 schematic components. Renderer reports
zero body overlaps but 15 rendered overlaps (including power symbols and labels).
Both screenshot attempts returned blank images despite nonzero component/wire
counts. Visual review is blocked; no schematic-readability acceptance is claimed.
BMI270, RGB indicators/PWM support and regulated motor circuit are still absent.
The full original-plan schematic request is not complete.

- C1/C2 Zen MPNs now match bom.md. Obsolete supplier SKUs were removed rather
  than transferred to different parts. Automatic lint/evaluation and the managed
  root build passed (15 components). No board regeneration or physical move ran.
- MAX17048 symbol/footprint assets materialized with provenance; wrapper and
  fixture validation are still pending. These are not yet integrated into Zen.
- Three preliminary reference STEP exports were cloud-built after repairing
  the Compound construction. All passed inspectable-solid checks only:
  - BAT1: `mechanical/components/bat1-reference/bat1-provisional-envelope.step`,
    revision `rev-31d573a35125bc3859d77bfbb0df98f03f3f52e703582cbb0b0603a178b34017`.
  - M1: `mechanical/components/m1-reference/qx-1027-reference-envelope.step`,
    revision `rev-04c4ff6a515c47ffbbf41770e17c54fde9752942c8d631e716872e359b7e279b`.
  - SW1: `mechanical/components/sw1-reference/pts841gk-body-only.step`,
    revision `rev-3d8be8e52fd355475e70c1d510022c33aa46fd0339a5aa678c6197930127afcf`.
- These are envelope references, not completion of the three detailed CAD gaps.
  SW1 actuator/leads, motor lead exit and purchased battery details remain open.
- Still required: complete GPIO/PWM allocation and motor supply, exact new part
  packages, all BOM support components, schematic layout, compact board outline
  and reviewed placement, modular enclosure/shutter, all-component assembly
  transforms and interference/service sweeps, electrical and printed validation.