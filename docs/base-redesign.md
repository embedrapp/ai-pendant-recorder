# Base-XIAO audio carrier revision

Implements docs/original-plan.md at schematic level. Prior source, BOM and routed
board are preserved in pcb/backups/pre-base-redesign/. The old routed board is
NOT a physical implementation of this revision; no regeneration or rerouting.

## Decisions and constraints
- Base Seeed XIAO ESP32S3 113991114; manufacturer SMD whole-board footprint,
  direct solder, no headers. Underside component clearance/recess needs review.
- Two layers, target 0.8 mm PCB; outline, enclosure, holes and component sides
  remain unfrozen. Battery separate XY cavity; no PCB over pouch.
- PDM prototype candidate IM69D130V01XTSA1 (69 dBA, 130 dBSPL AOP,
  4 x 3 x 1.2 mm). IM69D128SV01 is thinner (0.98 mm), 69 dBA, 128 dBSPL,
  520 uA high-performance / 180 uA low-power and deserves later comparison.
  IM69D130 has an exact established KiCad PG-LLGA-5-1 footprint. Manufacturer
  PDF retrieval is blocked by WAF; full indexed electrical/package review is
  still required before approval. This is not an acoustically validated choice.
- Hirose DM3D-SF push-pull microSD, 1.55 mm high. SPI, no live removal during
  writing. 3.3 V always supplied; flush/sleep card before deep sleep. No claim
  of hardware power gating, hot-plug ESD qualification or zero standby current.
- MAX17048 retained at 0x36; BMI270 retained at 0x68, INT1 now connected.
- Remove PCA9685 and external RGB LEDs. Use onboard GPIO21 user LED.
- Motor D0 both enables regulator and drives MOSFET; pulse high for haptics,
  low between events. Do not high-frequency PWM the LDO enable. Retain gate
  resistor/pulldown, LDO-enable pulldown, flyback to MOTOR_3V3 (not VBAT).
- Speaker remains provisional: 8 ohm CMS-16093-078L100, 0.7 W nominal;
  enforce <=2.37 Vrms differential and verify clipping/thermal behavior.
- Protected 1S pack, 4.2 V charge, 300–500 mAh, 11–18 mm wide,
  <=4–5.5 mm thick, roughly 45–65 mm long; >=500 mA continuous and documented
  pulse capability. NTC desirable, not wired without a documented pack.
- Existing connectors/controls retained provisionally, not declared low-profile
  mechanical fit. Manufacturing provider unspecified; do not manufacture yet.

## GPIO allocation (base board, no Sense expansion)
| Physical pin | ESP32 GPIO | Signal |
|---|---:|---|
| D0 | 1 | HAPTIC_ARM / motor gate via R7 |
| D1 | 2 | RECORD_BUTTON, active low |
| D2 | 3 | AMP_ENABLE; boot strap, external pulldown through R3/R2 |
| D3 | 4 | I2S_BCLK |
| D4 | 5 | FG_SDA |
| D5 | 6 | FG_SCL |
| D6 | 43 | I2S_LRCLK |
| D7 | 44 | I2S_DIN |
| D8 | 7 | SD clock through series resistor |
| D9 | 8 | SD MISO |
| D10 | 9 | SD MOSI |
| MTCK | 39 | SD_CS, pull-up |
| MTDO | 40 | BMI270 INT1 |
| MTDI | 41 | PDM data |
| MTMS | 42 | PDM clock through series resistor |

All 15 exposed general GPIO are allocated. External JTAG unavailable; USB
programming/debug remains. GPIO0/45/46 unchanged; GPIO3 strap must be checked
on actual board boot. SW2 is RESET standby, not battery disconnection and not
firmware deep sleep. IMU wake works only in software sleep, not held reset.

## Source evidence / unresolved review
- Seeed official wiki pin table retained in docs/redesign-evidence/xiao-wiki.md.
- Seeed official SMD footprint downloaded and SHA256-equal to existing asset:
  b093cd9a70feb3b00d0ee3f9d4b828b69aa605c28bd0c3e55347676db2994243.
- Seeed schematic index 15993097cd695d177af352f4664ca91290a99c833f51d122d1165ef222f9923c,
  page 4: GPIO39–42, SPI, regulator, charger. Download named v1.4 but sheet
  titled Sense V1.3 and internal filename V1.5. Wiki says 50 mA charger;
  sheet says 110 mA. Obtain supplier board revision and measure charge current.
- Hirose catalog index a19b36c3a960f67ebf0ab7fc5220423ca427c167cbb38a53e619b14226e8955d,
  page 9: socket pinout, 11.95 x 11.45 x 1.55 mm, 15.8 mm inserted envelope,
  no-trace regions. Upstream KiCad pad widths differ from latest recommendation;
  asset needs reconciliation and no-trace keepouts before layout acceptance.
- Infineon manufacturer IM69D130 datasheet v1.0 (2017-12-19), sections 2–6;
  web extraction confirms acoustic specs; KiCad Sensor_Audio.lib IM69D120 alias
  IM69D130 confirms DATA1/VDD2/CLOCK3/SELECT4/GND5. Full manufacturer pin,
  voltage, timing and land-pattern verification remains open.

## Power / acceptance
No runtime promise. Provisional peak envelope: radio/controller 350 mA,
SD 200 mA at 3.3 V, motor start 230 mA, speaker about 260 mA at 3 V for
0.7 W / 90% assumed efficiency: overlap can exceed 1 A. These are planning
allowances, not measured specifications. Prohibit upload+motor+playback and
avoid motor during SD writes until measured; verify XIAO regulator headroom.
For off/reset, standby, recording, playback, haptic, upload and USB-connected
states measure rail current, droop, charging termination and temperatures.
Charger is not an authoritative charge/full/fault interface. MAX17048 is not PCM.

Required: source build, exact-net assertions, independent ERC; package review;
new physical revision with placement/antenna/acoustic review, DRC/DFM;
firmware remap/build and bench audio/storage/power/wake tests. Firmware and
mechanical artifacts are unchanged and obsolete for this revision.