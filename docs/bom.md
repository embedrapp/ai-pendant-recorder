# AI Pendant Recorder — unified procurement BOM

Prototype procurement list for quantities below 10. Links are India-facing where available. Live quantity-10 pricing and stock checks are recorded in [Price and stock verification](#price-and-stock-verification), checked 2026-09-08 IST.

## Product assumptions

**Redesign checkpoint:** see [compact-redesign.md](compact-redesign.md). The
current Zen design is not yet this complete BOM. C1/C2 MPNs have been reconciled;
new circuits and their support parts remain pending. Do not procure a complete
assembly solely from the current generated PCB BOM.

**Motor supply correction required:** the retained QX-1027 datasheet specifies
2.5–3.5 V operation and 230 mA maximum starting/locked current at 3 V (pp3–4).
Direct protected BAT+ can reach 4.2 V and is not approved. The D1/BAT+ topology
below is historical pending a regulated MOTOR+ design; connect flyback cathode
to the actual motor-positive rail. The Robu motor identity remains unresolved.

- XIAO ESP32S3 Sense retains its camera, microphone, microSD, USB-C, Wi-Fi/BLE radio, antenna connector, and onboard single-cell LiPo charging/power-management path.
- Battery is a protected NOVA 603450, 3.7 V, 1100 mAh cell. Confirm PCM details, finished envelope, current rating, and connector compatibility before purchase.
- MAX17048 is installed directly on the redesigned PCB for battery voltage/state-of-charge reporting. It is not a charger or protection circuit.
- Camera privacy shutter, enclosure, antenna mount, LED light ports, pendant/keychain loop, battery retention, speaker cavity, and other enclosure features are custom 3D-printed/mechanical design items—not purchased BOM components.

## Unified final-product BOM

| Qty | Ref | Exact part | Supplier / India link | Status / notes |
|---:|---|---|---|---|
| 1 | U1 | Seeed Studio XIAO ESP32S3 Sense, MPN 113991115 | [DigiKey India](https://www.digikey.in/en/products/detail/seeed-technology-co-ltd/113991115/18724504), [Seeed](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html) | Selected. Bottom-mount for USB-C access; retain camera, microphone, microSD, Wi-Fi/BLE, and supplied antenna. |
| 1 | U2 | Analog Devices/Maxim MAX98357AETE+T, mono I2S Class-D amplifier | [DigiKey India](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX98357AETE-T/4936122) | Selected. BTL output only; neither speaker lead connects to GND. |
| 1 | U3 | Analog Devices/Maxim MAX17048G+T10, 8-TDFN-EP, 2 × 2 mm fuel gauge | [DigiKey India exact page](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX17048G-T10/3758921?s=N4IgTCBcDaILIEEAaBGA7ABgCwA4DiA1ACooYgC6AvkA) | Selected for direct PCB assembly. Fixed I²C address 0x36; reports voltage, estimated SOC, and rate. |
| 1 | U4 | Bosch BMI270, 6-axis accelerometer/gyroscope | [DigiKey India](https://www.digikey.in/en/products/detail/bosch-sensortec/BMI270/9974486) | Selected product candidate. Verify package, land pattern, required decoupling, and stock before PCB redesign. |
| 1 | SPK1 | Same Sky CMS-16093-078L100, 8 Ω, 0.7 W nominal, 16 × 9 × 3 mm | [Mouser India exact page](https://www.mouser.in/en/ProductDetail/Same-Sky/CMS-16093-078L100?qs=F5EMLAvA7ICF0RF14YtpPg%3D%3D&srsltid=AfmBOorX9JfqAb8TPj3nXFFX2kRklv_kxXp7DZXd5smgDBccuUt2hejx) | Selected. Requires an acoustic cavity; confirm lead termination/length. |
| 1 | BAT1 | NOVA 603450, 3.7 V, 1100 mAh protected LiPo | [Robu India](https://robu.in/product/nova-603450-1100mah-3-7v-micro-lipo-battery-pack/) | Selected provisionally. Listing shows protection PCB, attached 75 mm 26-AWG wires, and 2-pin plug; verify PCM, dimensions, current, polarity, and mating fit. |
| 1 | M1 | Flat 1027 mobile-phone vibration motor | [Robu India](https://robu.in/product/flat-1027-mobile-phone-vibration-motor/) | Selected haptic candidate, but the live URL currently renders **Flat 1034** (10 mm × 3.4 mm, 2.5–4 V, 90 mA max), not a verified 1027. Confirm the exact motor before release. Requires a transistor/MOSFET driver and flyback protection; never drive directly from ESP32 GPIO. |
| 1 | J1 | JST B2B-PH-K-S, 2-position, 2.00 mm PCB header | [DigiKey India](https://www.digikey.in/en/products/detail/jst-sales-america-inc/B2B-PH-K-S/926611) | Selected battery PCB header; confirm battery plug family, pitch, keying, and polarity. |
| 1 | J2 | JST BM02B-SRSS-TB(LF)(SN), 2-position, 1.00 mm SMT header | [DigiKey India](https://www.digikey.in/en/products/detail/jst-sales-america-inc/BM02B-SRSS-TB/926694) | Selected speaker PCB header; verify stock/lead time. |
| 1 | SW1 | C&K PTS841GKSMTR-LFS side-actuated SMT tactile switch | [DigiKey India](https://www.digikey.in/en/products/detail/c-k/PTS841-GK-SMTR-LFS/10445315) | Selected record button; verify land pattern and actuator alignment. |
| 1 | SW2 | C&K JS202011AQN DPDT ON-ON right-angle THT slide switch | [DigiKey India](https://www.digikey.in/en/products/detail/c-k/JS202011AQN/1640096) | Selected provisionally; reported backorder/stock risk. Do not substitute without mechanical/electrical review. |
| 2 | C1/C3 | Murata GCM188R71H104KA57J, 100 nF, 50 V, X7R, 0603 | [DigiKey India](https://www.digikey.in/en/products/detail/murata-electronics/GCM188R71H104KA57J/4380305) | C1 amplifier bypass; C3 local MAX17048 VDD bypass. |
| 1 | C2 | YAGEO CC0805KRX5R8BB106, 10 µF, 25 V, X5R, 0805 | [Mouser India](https://www.mouser.in/en/ProductDetail/YAGEO/CC0805KRX5R8BB106?qs=CNuWj9FTWYDQ%252BJODP2bXGA%3D%3D) | Selected bulk bypass; confirm DC-bias capacitance and packaging. |
| 2 | R1/R2 | YAGEO RC0603FR-07100KL, 100 kΩ, 1%, 0603 | [DigiKey India](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100KL/726889) | Selected. |
| 1 | R3 | YAGEO RC0603FR-072KL, 2 kΩ, 1%, 0603 | [DigiKey India](https://www.digikey.in/en/products/detail/yageo/RC0603FR-072KL/727009) | Existing amplifier-enable series resistor, not an RGB LED resistor. Six RGB current-limiting resistors remain to be specified. |
| 2 | R4/R5 | YAGEO RC0603FR-074K7L, 4.7 kΩ, 1%, 0603 | [DigiKey India](https://www.digikey.in/en/products/detail/yageo/RC0603FR-074K7L/727212) | I²C SDA/SCL pull-ups to 3.3 V, unless one verified pull-up pair already exists on the bus. |
| 1 | R6 | YAGEO RC0603FR-074K7L, 4.7 kΩ, 1%, 0603 | [DigiKey India](https://www.digikey.in/en/products/detail/yageo/RC0603FR-074K7L/727212) | Optional populated part for MAX17048 ALRT; otherwise DNP. |
| 2 | LED1/LED2 | Kingbright APGF0607G32B33R23-05, 0.65 × 0.65 × 0.25 mm full-color RGB SMD LED | [DigiKey India exact page](https://www.digikey.in/en/products/detail/kingbright/APGF0607G32B33R23-05/28948248) | Selected. Place at PCB edge beside small recessed/translucent enclosure light ports; use subtle low-PWM indication, not a large opening. |
| 1 | Q1 | Alpha & Omega Semiconductor AO3400A, 30 V N-channel logic-level MOSFET, SOT-23-3 | [DigiKey India exact page](https://www.digikey.in/en/products/detail/alpha-omega-semiconductor-inc/AO3400A/1855772) | **Finalized.** Low-side motor switch; suitable for 3.3 V GPIO drive and substantially exceeds the motor's approximately 60–90 mA operating/maximum current. Gate: ESP32 GPIO through R7; source: GND; drain: M1 negative terminal. |
| 1 | D1 | onsemi NSVR0320MW2T1G, 20 V, 1 A Schottky diode, SOD-323 | [element14 India exact page](https://in.element14.com/on-semiconductor/nsvr0320mw2t1g/schottky-diode-20v-sod-323/dp/2533249) | **Finalized.** Flyback diode across M1; cathode to protected BAT+/motor positive and anode to Q1 drain/motor negative. Current listing is orderable, but does not publish on-hand quantity and shows a long factory lead; confirm before release. |
| 1 | R7 | YAGEO RC0603FR-07100RL, 100 Ω, 1%, 100 mW, 0603 gate resistor | [DigiKey exact page](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100RL/726888), [Mouser India](https://www.mouser.in/en/ProductDetail/YAGEO/RC0603FR-07100RL?qs=NEN%2FsE%2FLsvPIwIWKCOS4%2FA%3D%3D) | Finalized. Series gate resistor between ESP32 GPIO and Q1 gate; reduces switching-edge ringing/EMI. |
| 1 | R8 | YAGEO RC0603FR-07100KL, 100 kΩ, 1%, 0603 gate pulldown | [DigiKey India exact page](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100KL/726889) | Keeps Q1 off while the ESP32 is resetting or unpowered. |
| 2 | TP3/TP4 | PCB test pads for FG_SDA and FG_SCL | PCB fabrication item | Recommended for fuel-gauge bring-up; no purchased component. |

## Motor enclosure connector — simplest finalized arrangement

Use the same **JST-PH 2.00 mm, 2-position** family already used for the battery. The motor remains attached to the enclosure wall; only its two wires run to a short detachable pigtail and board connector.

| Qty | Ref | Exact part | Supplier / India link | Status / notes |
|---:|---|---|---|---|
| 1 | J3 | JST B2B-PH-K-S, 2-position, 2.00 mm through-hole PCB header | [DigiKey India](https://www.digikey.in/en/products/detail/jst-sales-america-inc/B2B-PH-K-S/926611) | **Finalized.** Install at the PCB edge for easy enclosure assembly/service. Pin 1: MOTOR+; pin 2: MOTOR−/Q1 drain. |
| 1 | M1-HARNESS | Pre-terminated JST-PH 2-pin female cable/pigtail, approximately 150 mm | [Sunrom India JST-PH 2.0 mm](https://www.sunrom.com/c/jst-ph-20mm) | **Finalized as the easiest wiring method.** Select the 2-pin female PH cable, solder its two free wires to the motor leads, insulate/strain-relieve the joints, and plug the housing into J3. Do not use JST-XH or JST-SH. |

Do not add a second loose housing/contact procurement path for the motor. The pre-terminated PH pigtail avoids crimp tooling and eliminates manual contact insertion. Provide a small service loop, adhesive/clip strain relief, and enough slack for the enclosure half to open without pulling J3.

## Price and stock verification

Checked 2026-09-08 IST. The unit-price column is the supplier price per component when the order quantity is 10, and the extension is ten pieces of that MPN. `EXACT-10` means the supplier published a quantity-10 tier. `CARRIED-1` means no quantity-10 tier was exposed, so the quantity-1 price is carried forward as a conservative planning value; it is not a quote. `CLOSEST-TIER` uses the nearest published quantity band. Freight is excluded. GST is included only where the supplier page explicitly stated that it was included.

| BOM item / link | Qty in BOM | Unit @ 10 | 10-piece extension | Stock / availability at check | Basis |
|---|---:|---:|---:|---|---|
| [U1 — DigiKey 113991115](https://www.digikey.in/en/products/detail/seeed-technology-co-ltd/113991115/18724504) | 1 | ₹1,328.150 | ₹13,281.50 | 5,068 | CARRIED-1; no qty-10 tier exposed |
| [U1 — Seeed XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html) | 1 | $13.99 | $139.90 | In stock | EXACT-10+; shipping/tax excluded |
| [U2 — MAX98357AETE+T](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX98357AETE-T/4936122) | 1 | ₹294.676 | ₹2,946.76 | 28,797 | EXACT-10; Digi-Reel fee may apply |
| [U3 — MAX17048G+T10](https://www.digikey.in/en/products/detail/analog-devices-inc-maxim-integrated/MAX17048G-T10/3758921) | 1 | ₹334.329 | ₹3,343.29 | 26,351 | EXACT-10; purchase-limit/lead notices shown |
| [U4 — BMI270](https://www.digikey.in/en/products/detail/bosch-sensortec/BMI270/9974486) | 1 | ₹346.273 | ₹3,462.73 | 64,546 | Published qty-10 price |
| [SPK1 — CMS-16093-078L100](https://www.mouser.in/en/ProductDetail/Same-Sky/CMS-16093-078L100?qs=F5EMLAvA7ICF0RF14YtpPg%3D%3D) | 1 | ₹189.16 | ₹1,891.60 | 487; dispatch immediately | EXACT-10; 13-week factory lead also shown |
| [BAT1 — NOVA 603450](https://robu.in/product/nova-603450-1100mah-3-7v-micro-lipo-battery-pack/) | 1 | ₹239.00 incl. GST | ₹2,390.00 | In Stock | CARRIED-1; rendered page shows no qty-10 tier and lists MPN as N/A |
| [M1 — Robu link](https://robu.in/product/flat-1027-mobile-phone-vibration-motor/) | 1 | ₹29.00 incl. GST | ₹290.00 | In Stock | CARRIED-1 for the rendered Flat 1034 listing; not confirmation of the BOM’s Flat 1027 candidate |
| [J1/J3 — JST B2B-PH-K-S](https://www.digikey.in/en/products/detail/jst-sales-america-inc/B2B-PH-K-S/926611) | 2 | ₹9.555 | ₹95.55 | 261,174 | EXACT-10 |
| [J2 — JST BM02B-SRSS-TB](https://www.digikey.in/en/products/detail/jst-sales-america-inc/BM02B-SRSS-TB/926694) | 1 | ₹32.009 | ₹320.09 | 32,631; 16-week manufacturer lead | EXACT-10 |
| [SW1 — C&K PTS841-GK-SMTR-LFS](https://www.digikey.in/en/products/detail/c-k/PTS841-GK-SMTR-LFS/10445315) | 1 | ₹40.609 | ₹406.09 | 3,227 | EXACT-10 |
| [SW2 — C&K JS202011AQN](https://www.digikey.in/en/products/detail/c-k/JS202011AQN/1640096) | 1 | ₹68.414 | ₹684.14 | 7,480; 9,000 factory | EXACT-10 |
| [C1/C3 — Murata GCM188R71H104KA57J](https://www.digikey.in/en/products/detail/murata-electronics/GCM188R71H104KA57J/4380305) | 2 | ₹10.893 | ₹108.93 | 6,611,806 | EXACT-10 |
| [C2 — YAGEO CC0805KRX5R8BB106](https://www.mouser.in/en/ProductDetail/YAGEO/CC0805KRX5R8BB106?qs=CNuWj9FTWYDQ%252BJODP2bXGA%3D%3D) | 1 | ₹23.30 | ₹233.00 | 1,916; 16,000 on order | EXACT-10; 61-week factory lead shown |
| [R1/R2/R8 — YAGEO RC0603FR-07100KL](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100KL/726889) | 4 | ₹2.389 | ₹23.89 | 2,204,756 | EXACT-10 |
| [R3 — YAGEO RC0603FR-072KL](https://www.digikey.in/en/products/detail/yageo/RC0603FR-072KL/727009) | 1 | ₹2.389 | ₹23.89 | 618,847 | EXACT-10 |
| [R4/R5/R6 — YAGEO RC0603FR-074K7L](https://www.digikey.in/en/products/detail/yageo/RC0603FR-074K7L/727212) | 3 | ₹2.389 | ₹23.89 | 1,473,985 | EXACT-10; R6 is optional/DNP |
| [LED1/LED2 — Kingbright APGF0607G32B33R23-05](https://www.digikey.in/en/products/detail/kingbright/APGF0607G32B33R23-05/28948248) | 2 | ₹44.144 | ₹441.44 | 520; limited | EXACT-10 |
| [Q1 — AO3400A](https://www.digikey.in/en/products/detail/alpha-omega-semiconductor-inc/AO3400A/1855772) | 1 | ₹30.767 | ₹307.67 | 108,135 | EXACT-10 |
| [D1 — NSVR0320MW2T1G](https://in.element14.com/on-semiconductor/nsvr0320mw2t1g/schottky-diode-20v-sod-323/dp/2533249) | 1 | ₹62.180 | ₹621.80 | Orderable; on-hand count not published; 21-week lead | CLOSEST-TIER; 5+ tier projected to 10 |
| [R7 — DigiKey RC0603FR-07100RL](https://www.digikey.in/en/products/detail/yageo/RC0603FR-07100RL/726888) | 1 | ₹2.389 | ₹23.89 | 1,047,451 | EXACT-10 |
| [R7 — Mouser alternative](https://www.mouser.in/en/ProductDetail/YAGEO/RC0603FR-07100RL?qs=NEN%2FsE%2FLsvPIwIWKCOS4%2FA%3D%3D) | 1 | ₹1.30 | ₹13.00 | 4,763,374 | EXACT-10; MouseReel fee may apply |
| [M1-HARNESS — Sunrom item 8074](https://www.sunrom.com/p/2-pin-jst-ph-2mm-teflon-ptfe-24732-one-side-female-15cm-wire) | 1 | ₹17.25 | ₹172.50 | 227 ready | Published 1–49 tier; BOM category link is [JST-PH 2.0 mm](https://www.sunrom.com/c/jst-ph-20mm) |
| [7Semi MAX17048 breakout — IoTCart](https://iotcart.in/product/max17048-li-poly-li-ion-fuel-gauge-breakout-board-mini-7semi) | 1 dev-only | ₹768.60 | ₹7,686.00 | In stock; backorder available | CARRIED-1; price shown incl. GST, no reliable qty-10 tier |
| [Temporary BMI270 breakout — Hubtronics](https://hubtronics.in/imu-bmi270-stemma-breakout) | 1 dev-only | ₹584.00 | ₹5,840.00 | Out of stock; notify | CARRIED-1; price shown incl. GST |
| Temporary motor test setup | 1 dev-only | ₹29.00 incl. GST | ₹290.00 | In Stock | Same rendered Flat 1034 listing as M1; exact 1027 identity remains unresolved |
| TP3/TP4 test pads and custom mechanical items | — | N/A | N/A | N/A | PCB/custom fabrication features, not purchased components |

The Robu battery and motor values are current rendered-page values. The motor identity is still unresolved because the supplied 1027 URL currently serves a Flat 1034 listing. Do not treat projected `CARRIED-1` extensions as purchase commitments.

## MAX17048 circuit requirements

- VDD connects to protected BAT+; GND and CTG connect to protected battery/system negative; exposed pad connects to GND.
- MAX17048 pin CELL is internally unconnected and must remain electrically unconnected.
- C3 is placed directly between VDD and GND.
- QSTRT is tied to GND for normal software-controlled operation.
- SDA/SCL connect to XIAO I²C and use one effective 3.3 V pull-up pair only.
- ALRT may be left unconnected for polling, or routed to an ESP32 GPIO with R6 populated.
- MAX17048 does not replace the battery PCM, charger, regulator, or safety protection.

## Dev-only / bench-validation list

These parts are for development or bring-up and are not installed in the final pendant.

| Qty | Part | Link | Purpose |
|---:|---|---|---|
| 1 | 7Semi MAX17048 LiPo/Li-ion fuel-gauge breakout | [IoTCart India](https://iotcart.in/product/max17048-li-poly-li-ion-fuel-gauge-breakout-board-mini-7semi) | Bench prototype for testing I²C fuel-gauge readings before the bare MAX17048 PCB implementation. |
| 1 | Temporary BMI270 breakout, if used for firmware bring-up | [Hubtronics India](https://hubtronics.in/imu-bmi270-stemma-breakout) | Firmware/prototyping only; final product uses the bare BMI270 IC. |
| 1 | Temporary motor/driver test setup | Use Robu motor link above | Bench testing of motor current, vibration, driver selection, and haptic patterns before PCB integration. |

## Not procurement BOM: custom mechanical items

These are designed and 3D-printed or fabricated as part of the enclosure, not purchased as electronic BOM components:

- Opaque camera privacy shutter
- Pendant/keychain attachment loop with reinforced rounded through-hole
- Antenna adhesive wall mount and internal antenna keepout
- Edge LED light ports/light-pipe recesses
- Enclosure shell, PCB standoffs, battery pocket/retention, speaker cavity/grille/gasket
- Magnets, fasteners, adhesive, strain relief, and acoustic damping, unless later assigned exact purchased parts

## Final procurement gates

1. Confirm live stock, price, pack size, GST/freight, and lifecycle for every selected MPN.
2. Obtain battery PCM/current/dimension documentation and verify J1 mating fit and polarity.
3. Finalize Q1, D1, BMI270 support passives, and motor-driver values from the selected motor specifications.
4. Verify SW2 availability or approve a mechanically/electrically equivalent alternate.
5. Verify LED polarity/pinout and validate visibility through the small enclosure light ports.
6. Complete PCB placement, routing, ERC/DRC/DFM, charging, battery, haptic, acoustic, thermal, RF, and enclosure-fit validation before manufacturing approval.
