# Base-XIAO recorder with 5x5 RGB matrix — procurement BOM (DRAFT)

**Not released for purchase/assembly.** Supersedes the Sense/603450/RGB BOM.
Generated from `pcb/bom.csv`; electrical source refs may differ from physical KiCad refs.
Prior BOM and historical prices: `pcb/backups/pre-base-redesign/bom.md`.
Live stock and price were checked only for BAT1 at selection time; all sourcing
remains time-sensitive. See [validation and GPIO map](base-redesign.md).

## Carrier PCB components

| Qty | Source refs | MPN | Value / function | Existing sourcing link |
|---:|---|---|---|---|
| 6 | C1 / C3 / C4 / C5 / C9 / C10 | GCM188R71H104KA57J | 100nF 50V X7R | [existing supplier](https://www.digikey.in/en/products/detail/murata-electronics/GCM188R71H104KA57J/4380305) |
| 4 | C2 / C7 / C8 / C11 | CC0805KRX5R8BB106 | 10uF 25V X5R | [existing supplier](https://www.mouser.in/en/ProductDetail/YAGEO/CC0805KRX5R8BB106?qs=CNuWj9FTWYDQ%252BJODP2bXGA%3D%3D) |
| 1 | D1 | NSVR0320MW2T1G | NSVR0320 | [existing supplier](https://in.element14.com/on-semiconductor/nsvr0320mw2t1g/schottky-diode-20v-sod-323/dp/2533249) |
| 2 | J1 / J3 | B2B-PH-K-S | JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical | [existing supplier](https://www.digikey.in/en/products/detail/jst-sales-america-inc/B2B-PH-K-S/926611) |
| 1 | J4 | 104031-0811 | Molex 1.42 mm push-pull microSD socket with detect | [Molex](https://www.molex.com/en-us/products/part-detail/1040310811) |
| 1 | MK1 | IM69D130V01XTSA1 | IM69D130 | **Link needed** |
| 1 | Q1 | AO3400A | SOT-23 | [existing supplier](https://www.digikey.in/en/products/detail/alpha-omega-semiconductor-inc/AO3400A/1855772) |
| 5 | R1 / R8 / R23 / R26 / R27 | RC0603FR-07100KL | 100k 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100KL/726889) |
| 2 | R4 / R5 | RC0603FR-074K7L | 4.7k 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-074K7L/727212) |
| 1 | R7 | RC0603FR-07100RL | 100 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100RL/726888) |
| 2 | R16 / R17 | RC0603FR-0733RL | 33 100mW | **Link needed** |
| 5 | R18 / R19 / R20 / R21 / R22 | RC0603FR-0747KL | 47k 100mW | **Link needed** |
| 1 | SW1 | PTS841GKSMTR LFS | PTS841GK | **Link needed** |
| 1 | SW2 | JS202011AQN | SW_CK_JS202011AQN_DPDT_Angled | [existing supplier](https://www.digikey.in/en/products/detail/c-k/JS202011AQN/1640096) |
| 1 | U1 | 113991114 | XIAO | [Seeed base board](https://www.seeedstudio.com/XIAO-ESP32S3-p-5627.html); India supplier link needed |
| 1 | U3 | MAX17048G+T10 | kicad_footprint | [existing supplier](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX17048G-T10/3758921?s=N4IgTCBcDaILIEEAaBGA7ABgCwA4DiA1ACooYgC6AvkA) |
| 1 | U4 | BMI270 | BMI270 | [existing supplier](https://www.digikey.in/en/products/detail/bosch-sensortec/BMI270/9974486) |
| 1 | U6 | AP2112K-3.3TRG1 | AP2112K_3V3 | **Link needed** |
| 25 | LED1–LED25 | WS2812C-2020-V1 | 2.0 mm addressable RGB, 5 mA/channel | [LCSC C2976072](https://www.lcsc.com/product-detail/C2976072.html) |
| 25 | C15–C39 | GRM155R71C104KA88D | 100 nF 16 V X7R 0402, one per pixel | [Murata](https://pim.murata.com/en-us/pim/details?partNum=GRM155R71C104KA88D) |
| 1 | U5 | TPS61023DRLR | 5 V synchronous boost converter | [TI](https://www.ti.com/product/TPS61023) |
| 1 | U7 | TPS22918DBVR | 2 A load switch, switched LED rail | [TI](https://www.ti.com/product/TPS22918) |
| 1 | L1 | XEL4030-102MEC | 1 uH shielded power inductor | [Coilcraft](https://www.coilcraft.com/en-us/products/power/shielded-inductors/molded-inductor/xel/xel4030/xel4030-102/) |
| 2 | C13 / C14 | GRM21BR61A226ME44L | 22 uF 10 V X5R 0805 | [Murata](https://pim.murata.com/en-sg/pim/details?partNum=GRM21BR61A226ME44L) |
| 1 | R25 | RC0603FR-07732KL | 732k 1% boost feedback | [DigiKey](https://www.digikey.com/en/products/detail/yageo/RC0603FR-07732KL/727376) |
| 1 | R28 | RC0603FR-07470RL | 470 ohm LED data series resistor | **Link needed** |
| 1 | C40 | GRM1555C1E102JA01D | 1 nF 25 V C0G 0402, TPS22918 rise-time control | [Murata](https://pim.murata.com/en-us/pim/details?partNum=GRM1555C1E102JA01D) |

## Off-board / assembly procurement

| Qty | Item | Requirement / source status |
|---:|---|---|
| 1 | BAT1 Adafruit 1578 / PKCELL LP-503035 family, protected 1S LiPo | 3.7 V nominal, 500 mAh, 4.2 V CC/CV, 1C / 500 mA maximum continuous discharge, PCM and two-wire JST-PH lead. Conservative CAD pack envelope 30.1 x 36.0 x 5.1 mm; tray reserves 30.1 x 36.0 x 6.1 mm including 1 mm expansion allowance. No NTC. [Adafruit product 1578](https://www.adafruit.com/product/1578) (USD 7.95 and in stock when selected); [manufacturer datasheet](https://cdn-shop.adafruit.com/product-files/1578/Datasheet.pdf); [India distributor family listing](https://www.fabtolab.com/lithium-polmer-1s-battery) (exact 1578 option stock/price must be confirmed). **Selected for tray design, not yet purchase-approved.** |
| 1 | M1 exact vibration motor TBD | Old Robu 1027 URL served 1034. **Replacement exact link with start/stall current and dimensions required.** Must tolerate regulated 3.3 V. |
| 1 | microSD card, exact MPN/capacity TBD | Prefer traceable high-endurance 16–32 GB FAT32 for prototype; **link needed**. Qualify write latency and peak/standby current. |
| 1 set | Battery and motor harnesses | J1/J3 PH 2 mm; confirm polarity, wire length, and connector orientation. Motor PH pigtail has prior Sunrom link. |
| 1 set | Microphone acoustic gasket / dust mesh | **Supplier links needed**, thickness and acoustic impedance TBD after port design. |
| 1 | XIAO-compatible 2.4 GHz antenna | Confirm supplied with base SKU; otherwise exact antenna link/drawing needed. |

## Changes and purchasing cautions

- Removed Sense 113991115 expansion/camera/SD/mic assembly, camera mechanics, NOVA 603450 battery, PCA9685, two RGB LEDs, C6 and R9–R14.
- Selected BAT1 Adafruit 1578 as the active tray basis. Adafruit documents
  overcharge, over-discharge and short-circuit protection; the supplier drawing
  shows a 1S PCM. Exact overcurrent threshold remains a procurement gate.
- Adafruit states that this pack has no thermistor. Existing two-pin J1 supports
  VBAT and GND only, so it cannot monitor an NTC. Confirm charger compatibility,
  delivered connector polarity, and current before energizing the assembly.
- Adafruit lists 29 x 36 x 4.75 mm while its attached pack drawing shows
  30 +/-0.1 x 35 +/-0.1 x 5 +/-0.1 mm. The mechanical design uses the
  conservative union rather than treating either nominal description as exact.
- BAT1 documentation: indexed datasheet `ds_dcee32f4e0c985211bc8`, tray STEP
  `mechanical/exports/pendant-battery-tray-adafruit-1578.step`, and design notes
  `mechanical/front-battery-notes.md`. UN38.3/MSDS applicability, India shipping,
  delivered-pack metrology and load/thermal testing remain required.
- Added base 113991114, IM69D130V01XTSA1 microphone, Molex 104031-0811 socket, C9/C10/C11, and R16–R23. The former DM3D-SF candidate is superseded.
- New unique resistors needing links: RC0603FR-0733RL (33 ohm, 2 pcs), RC0603FR-0747KL (47k, 5 pcs).
- AP2112K-3.3TRG1 was already in the circuit but lacks a saved sourcing link.
- Additional 100nF/10uF/100k parts reuse existing MPN links; no new passive selection needed for those.
- H1–H4 and TP3/TP4 are PCB features, not purchased components. Mounting hardware remains mechanical-design TBD.
- Flyback D1 cathode is MOTOR_3V3, NOT VBAT.
- J1/J3 through-hole PH headers and SW2 remain provisional thickness risks.
- Speaker, MAX98357A amplifier, speaker connector, gain/shutdown network, and speaker mechanics are removed.
- A 5x5 WS2812C-2020-V1 matrix is the central visual interface. Its 5 V rail is firmware-enabled and must use a brightness/current budget; do not combine full-white output with motor start/stall load.
- TPS22918 U7 is now present between BOOST_5V and LED_5V. C40 controls rise time and QOD directly discharges LED_5V when disabled; bench inrush and thermal validation remain mandatory.
- Microphone is frozen as IM69D130V01XTSA1. J4 is frozen as active Molex 104031-0811; its manufacturer drawing and KiCad footprint establish the land pattern, but card-access and component-envelope clearance still require revised placement review.

## Confirmed product decisions

- Retain JS202011AQN and use one pole for standby/reset; the second pole remains intentionally unconnected.
- Share one GPIO between TPS61023 EN and TPS22918 ON.
- Charge the protected Adafruit 1578 through the XIAO ESP32S3 onboard battery charger/USB path, subject to polarity and bench compatibility verification.
- Limit the LED rail design target to 100 mA; full-matrix white is prohibited.
- Freeze IM69D130V01XTSA1, Molex 104031-0811, and the existing regulated 3.3 V haptic architecture. The exact motor remains a downstream procurement/fit qualification.
