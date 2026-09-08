# RGB/PWM and regulated haptics circuit

Implemented in `pcb/ai_pendant_recorder.zen`; firmware and physical board unchanged.

## Connections and operation
- U5 PCA9685PW,118 at I2C 0x40, all six address straps low; shared R4/R5
  pull-ups only. Internal clock (EXTCLK grounded), OE grounded, 3.3 V supply/C6.
- PWM0–2 = LED1 R/G/B, PWM3–5 = LED2 R/G/B. Exact Kingbright
  APGF0607G32B33R23-05 common-anode LEDs, anodes at V3V3. Six 2 kΩ
  resistors R9–14 limit instantaneous current to <1.7 mA even with zero Vf.
  Actual blue/green current and visibility near 3.3 V require bench testing.
  Push-pull output mode is required: low lights LED, high extinguishes it.
  POR outputs are low, so LEDs initially illuminate at resistor-limited current;
  they are NOT guaranteed dark or a trustworthy recording indication before init.
- PWM6 drives Q1 through R7=100 Ω; R8=100 kΩ gate-to-ground. High runs motor.
  Use the common PWM frequency within PCA9685 limits (e.g. 1 kHz); motor noise,
  switching loss and optical flicker require bench review.
- D0/GPIO1 independently arms U6 AP2112K-3.3TRG1; R15=100 kΩ defaults off.
  U6 is supplied from protected BAT+, not the XIAO 3.3 V rail. Its 3.3 V output
  feeds J3 pin1; pin2 is Q1 drain. D1 cathode is MOTOR_3V3, anode Q1 drain.
  Initialize PWM6 low before arming. Disarm on stop/fault/standby; reset's
  high-impedance GPIO allows R15 to disable supply even if PWM registers persist.
- C7/C8 10 µF input/output bypass; ensure >1 µF effective after DC bias/tolerance.
  No battery charger was added. D8–D10 and Sense internal pins untouched.

## Grounding and corrections
- Kingbright local datasheet SHA256 43d8fc8d3f7e39f0f9c21c2bf722aae6e65334d89e6bc0cbe2543b41e386283e,
  p1: pin1 anode, 2 green, 3 blue, 4 red; 0.25 mm lands with 0.15 mm gaps.
  Stencil 80% open area/80–100 µm is a manufacturing gate, not yet enforced.
- PCA9685 indexed ds_b09c802523b445b70995 chunks 12–14,49: TSSOP pins
  LED0=6, VSS=14, OE=23, A5=24. Published library symbol metadata was WRONG;
  private corrected symbol used, original retained unused. Package footprint reused.
- AP2112 indexed ds_6ea4cad5e5943d92f8bb chunks 4,35: VIN1/GND2/EN3/NC4/VOUT5.
  Published library EN/GND numbering was WRONG; private symbol and manufacturer
  suggested lands used. Regulator is 600 mA rated, subject to thermal limits.
- onsemi retained datasheet p1,3: NSVR0320MW2T1G K1/A2; lands 0.63×0.83 mm,
  centres 2.23 mm apart. Diode dissipation limit 200 mW at 25°C must be respected.
- Q1 uses the installed exact AO3400A package and G1/S2/D3 mapping.
  Asset generation is reproducible with `pcb/components/generate_indicator_assets.py`.

## Limits and acceptance

Validation run: package sync, managed root build (43 components), exact netlist
inventory (65 nets), renderer pin/net inspection, schematic screenshot and ERC.
ERC: zero errors/warnings; 70 redundant-name style advice. Drawing remains
visually draft with label overlaps. The untouched old board fails DRC and must
not be fabricated as this circuit. No runtime, thermal or motor-load test ran.
Motor selection remains the BOM's Flat 1027 candidate; Robu URL discrepancy
is not resolved by this circuit. Nominal 3.3 V avoids direct 4.2 V battery drive.
QX reference starts at up to 230 mA at 3 V; at 3.3 V allow approximately 260 mA
for preliminary budgeting, not a verified maximum. U6 nominal dissipation is
about (4.2−3.3)×0.26=0.234 W during start; copper/temperature and stalled-motor
tests are required. Dropout at depleted battery may reduce vibration or prevent
starting. Firmware must bound haptic pulse duration and disable at low battery.
Neither LDO current limit nor MOSFET rating is a substitute for motor stall protection.

No new exact STEP models for U5/U6 or physical placement are claimed. TSSOP28
is a larger but inspectable prototype driver, not proof of minimum board area.
Review all custom footprints, assembly tolerances, shared bus current, rail
transients, RF/audio coupling, startup behaviour and LED visibility before release.