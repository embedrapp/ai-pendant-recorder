# Datasheet-grounded schematic review — base XIAO revision

Reviewed 2026-09-09 against the locally indexed Infineon IM69D130, Hirose DM3,
and Seeed XIAO ESP32S3 113991114 documents. This review covers schematic intent
and component mappings. It does not validate the obsolete routed PCB.

## Result

The new microphone, socket, and base-XIAO electrical mappings are internally
consistent and the Zen source builds. Independent ERC reports 0 errors and 0
warnings (64 style advice items). The schematic remains a draft because the new
physical revision has not been placed or routed and two footprint constraints
must be corrected before layout acceptance.

## U1 — Seeed 113991114

- The wrapper uses the exact base-board MPN and the official whole-board SMD
  footprint. It exposes all 14 castellated pins plus MTDI, MTDO, EN, GND, MTMS,
  MTCK, USB D-/D+, BAT+, BAT-, and the central thermal pad.
- The source maps MTCK/GPIO39 to SD chip select, MTDO/GPIO40 to BMI270 INT1,
  MTDI/GPIO41 to PDM DATA, and MTMS/GPIO42 to PDM CLOCK. These agree with the
  retained official pin table and schematic intent.
- VBUS and USB D+/D- are explicitly unused; USB remains available on the XIAO's
  own connector. The central thermal pad is explicitly electrically unconnected.
- The exact product datasheet specifies 21 x 17.8 mm and a nominal charging
  current of 50 mA fast / 3.8 mA trickle. The final protected 1S pack must be
  compatible with that charge rate; the charger is not a battery protection IC.
- Mechanical access to USB-C, buttons, antenna/U.FL area, BAT pads, and underside
  pads is a placement requirement, not a schematic validation.

## MK1 — IM69D130V01XTSA1

- Pin mapping is exact: 1 DATA, 2 VDD, 3 CLOCK, 4 SELECT, 5 GND. SELECT is tied
  low, which fixes the microphone to one PDM edge/channel and matches firmware's
  left-channel selection assumption.
- 3.3 V is inside the 1.62–3.6 V operating range but leaves only 0.3 V to the
  maximum recommended supply; rail overshoot must remain below the 4 V absolute
  maximum on any pin.
- C9 provides the required 100 nF VDD bypass. It must be placed directly at pins
  2/5 with a short return path for the stated SNR performance.
- R23 holds CLOCK low when the MCU is inactive, selecting the datasheet's
  clock-off mode. R16 is a source-series CLOCK damper. The datasheet instead
  identifies approximately 100 ohm as an optional DATA termination for ringing;
  decide this from final trace length or measured ringing rather than adding a
  new BOM item unconditionally.
- The footprint pad numbers, 4 x 3 mm body, and 0.8 mm PCB acoustic opening agree
  with the manufacturer drawing. The opening and stencil geometry are present.
  Acoustic enclosure alignment and contamination protection remain unvalidated.

## J4 — Hirose DM3D-SF

- Pins 1–8 map correctly to DAT2, CD/DAT3 (SPI CS), CMD (SPI MOSI), VDD, CLK,
  VSS, DAT0 (SPI MISO), and DAT1. Shield tabs are grounded. The normally-open
  detect switch is explicitly unused.
- R18–R22 pull up DAT3/CS, CMD/MOSI, DAT0/MISO, DAT1, and DAT2. No pull-up is
  placed on CLK. This is consistent with entering and operating SPI mode.
- R17 is a source-series CLK damper. C10 (100 nF) and C11 (10 uF) provide local
  card-supply decoupling/bulk capacitance, subject to close physical placement.
- **Blocking footprint finding:** the current footprint uses 0.70 mm signal-pad
  width, while the reviewed Hirose recommendation shows 0.55 mm. Reconcile the
  exact land pattern before fabrication.
- **Blocking layout finding:** the footprint only draws `KEEPOUT` graphics; it
  does not encode enforceable copper rule areas for the manufacturer's
  “No conductive traces” regions. Add real keepouts before routing.

## Cross-artifact findings

- `src/main.cpp` still says `sdCS=21`, while this schematic assigns SD_CS to
  MTCK/GPIO39. Firmware also sets `ampEnable=5`, while the schematic assigns
  AMP_ENABLE to D2/GPIO3. Firmware is therefore not pin-compatible with this
  schematic revision and must be remapped before hardware testing.
- The current `pcb/layout/layout.kicad_pcb` is the preserved pre-redesign board:
  DRC references removed U5, D2/D3, R9–R14 and reports 115 errors plus 32
  warnings. Those results are evidence that the old board is stale, not a DRC
  verdict on a generated base-revision layout.
- Schematic rendering has no component-body overlaps, but reports 49 rendered
  envelope collisions and 26 close pairs. Connectivity is traceable, yet label
  and power-symbol clutter should be cleaned in a separate drawing-layout pass.

## Required next gates

1. Correct the DM3D-SF signal pads and encode its no-trace rule areas.
2. Freeze board outline/mechanics, then place U1, J4, and MK1 around connector,
   antenna, card-access, acoustic-port, and underside-clearance constraints.
3. Place C9 at MK1 and C10/C11 at J4 before routing; evaluate DATA termination.
4. Generate and route the new physical board, then run ERC, DRC, DFM, and visual
   layer review on that artifact.
5. Remap firmware pins and perform bench audio, storage, charging, rail-droop,
   and coexistence tests with the selected protected battery pack.