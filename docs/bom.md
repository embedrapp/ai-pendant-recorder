# Base-XIAO audio carrier — procurement BOM (DRAFT)

**Not released for purchase/assembly.** Supersedes the Sense/603450/RGB BOM.
Generated from `pcb/bom.csv`; electrical source refs may differ from physical KiCad refs.
Prior BOM and historical prices: `pcb/backups/pre-base-redesign/bom.md`.
No live stock or prices checked in this revision. See [validation and GPIO map](base-redesign.md).

## Carrier PCB components

| Qty | Source refs | MPN | Value / function | Existing sourcing link |
|---:|---|---|---|---|
| 6 | C1 / C3 / C4 / C5 / C9 / C10 | GCM188R71H104KA57J | 100nF 50V X7R | [existing supplier](https://www.digikey.in/en/products/detail/murata-electronics/GCM188R71H104KA57J/4380305) |
| 4 | C2 / C7 / C8 / C11 | CC0805KRX5R8BB106 | 10uF 25V X5R | [existing supplier](https://www.mouser.in/en/ProductDetail/YAGEO/CC0805KRX5R8BB106?qs=CNuWj9FTWYDQ%252BJODP2bXGA%3D%3D) |
| 1 | D1 | NSVR0320MW2T1G | NSVR0320 | [existing supplier](https://in.element14.com/on-semiconductor/nsvr0320mw2t1g/schottky-diode-20v-sod-323/dp/2533249) |
| 2 | J1 / J3 | B2B-PH-K-S | JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical | [existing supplier](https://www.digikey.in/en/products/detail/jst-sales-america-inc/B2B-PH-K-S/926611) |
| 1 | J2 | BM02B-SRSS-TB(LF)(SN) | BM02B | [existing supplier](https://www.digikey.in/en/products/detail/jst-sales-america-inc/BM02B-SRSS-TB/926694) |
| 1 | J4 | DM3D-SF | DM3D-SF | **Link needed** |
| 1 | MK1 | IM69D130V01XTSA1 | IM69D130 | **Link needed** |
| 1 | Q1 | AO3400A | SOT-23 | [existing supplier](https://www.digikey.in/en/products/detail/alpha-omega-semiconductor-inc/AO3400A/1855772) |
| 6 | R1 / R2 / R8 / R15 / R23 / R24 | RC0603FR-07100KL | 100k 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100KL/726889) |
| 1 | R3 | RC0603FR-072KL | 2k 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-072KL/727009) |
| 2 | R4 / R5 | RC0603FR-074K7L | 4.7k 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-074K7L/727212) |
| 1 | R7 | RC0603FR-07100RL | 100 100mW | [existing supplier](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100RL/726888) |
| 2 | R16 / R17 | RC0603FR-0733RL | 33 100mW | **Link needed** |
| 5 | R18 / R19 / R20 / R21 / R22 | RC0603FR-0747KL | 47k 100mW | **Link needed** |
| 1 | SW1 | PTS841GKSMTR LFS | PTS841GK | **Link needed** |
| 1 | SW2 | JS202011AQN | SW_CK_JS202011AQN_DPDT_Angled | [existing supplier](https://www.digikey.in/en/products/detail/c-k/JS202011AQN/1640096) |
| 1 | U1 | 113991114 | XIAO | [Seeed base board](https://www.seeedstudio.com/XIAO-ESP32S3-p-5627.html); India supplier link needed |
| 1 | U2 | MAX98357AETE+T | kicad_footprint | [existing supplier](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX98357AETE-T/4936122) |
| 1 | U3 | MAX17048G+T10 | kicad_footprint | [existing supplier](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX17048G-T10/3758921?s=N4IgTCBcDaILIEEAaBGA7ABgCwA4DiA1ACooYgC6AvkA) |
| 1 | U4 | BMI270 | BMI270 | [existing supplier](https://www.digikey.in/en/products/detail/bosch-sensortec/BMI270/9974486) |
| 1 | U6 | AP2112K-3.3TRG1 | AP2112K_3V3 | **Link needed** |

## Off-board / assembly procurement

| Qty | Item | Requirement / source status |
|---:|---|---|
| 1 | BAT1 protected 1S LiPo, exact MPN TBD | 300–500 mAh, 11–18 mm finished width, <=4–5.5 mm thick, 45–65 mm long; >=500 mA continuous plus documented pulse, 4.20 V charge, PCM, preferred 10k NTC. **New link and manufacturer drawing required.** |
| 1 | SPK1 Same Sky CMS-16093-078L100 | Retained provisionally, 8 ohm / 0.7 W; existing Mouser link in archived BOM. R24 selects 3 dB gain; output limit and cavity bench validation required. |
| 1 | M1 exact vibration motor TBD | Old Robu 1027 URL served 1034. **Replacement exact link with start/stall current and dimensions required.** Must tolerate regulated 3.3 V. |
| 1 | microSD card, exact MPN/capacity TBD | Prefer traceable high-endurance 16–32 GB FAT32 for prototype; **link needed**. Qualify write latency and peak/standby current. |
| 1 set | Battery, speaker and motor harnesses | J1/J3 PH 2 mm, J2 SH 1 mm; confirm polarity, wire length, connector orientation. Motor PH pigtail has prior Sunrom link; **exact battery/speaker mating leads needed**. |
| 1 set | Microphone acoustic gasket / dust mesh | **Supplier links needed**, thickness and acoustic impedance TBD after port design. |
| 1 | XIAO-compatible 2.4 GHz antenna | Confirm supplied with base SKU; otherwise exact antenna link/drawing needed. |

## Changes and purchasing cautions

- Removed Sense 113991115 expansion/camera/SD/mic assembly, camera mechanics, NOVA 603450 battery, PCA9685, two RGB LEDs, C6 and R9–R14.
- Added base 113991114, candidate IM69D130V01XTSA1, DM3D-SF socket, C9/C10/C11, R16–R24.
- New unique resistors needing links: RC0603FR-0733RL (33 ohm, 2 pcs), RC0603FR-0747KL (47k, 5 pcs).
- AP2112K-3.3TRG1 was already in the circuit but lacks a saved sourcing link.
- Additional 100nF/10uF/100k parts reuse existing MPN links; no new passive selection needed for those.
- H1–H4 and TP3/TP4 are PCB features, not purchased components. Mounting hardware remains mechanical-design TBD.
- Flyback D1 cathode is MOTOR_3V3, NOT VBAT. Speaker terminals are differential, neither grounded.
- J1/J3 through-hole PH headers and SW2 remain provisional thickness risks.
- No external RGB indication. Base board GPIO21 user LED is reused.
- Candidate microphone package/electrical review and socket land-pattern/no-trace regions are unresolved; do not substitute or freeze layout from this draft.
