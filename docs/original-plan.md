# AI Second Brain Pendant — Original Implementation Plan

## Current-state findings

- Start from the existing electronics-plus-firmware scaffold without replacing user files.
- Use the exact Seeed Studio XIAO ESP32S3 Sense (SKU 113991115) as the controller.
- Use the MAX98357A audio amplifier as the speaker driver; if no installable module package exists, author an exact local IC wrapper from the datasheet.
- Resolve exact battery, speaker, switch, connector, and enclosure dimensions before manufacturing claims.

## Confirmed decisions

- Firmware target: ESP32-S3 DevKitC-1-compatible PlatformIO environment, because the installed target catalog lacks an exact XIAO target.
- Audio: direct MAX98357AETE+T IC implementation.
- Initial mechanical concept: protected 3.7 V, 500 mAh LiPo envelope.

## Project configuration

- Repair `embedr.yaml` and `platformio.ini` to use the ESP32-S3-compatible environment.
- Preserve the existing project identity and scaffold.
- Add firmware configuration placeholders and documentation without committing credentials.

## PCB design

- Install the exact XIAO Sense component package.
- Create an exact local MAX98357AETE+T wrapper with verified pins, footprint, exposed pad, and datasheet provenance.
- Add the XIAO module, amplifier, bypass capacitors, I2S nets, speaker output, record button, battery input, shutdown circuitry, test points, and mechanical interfaces.
- Use two copper layers unless routing or return-path analysis proves that more are required.
- Document voltage, current, battery, GPIO, RF, microSD, camera, enclosure, and acceptance assumptions.

## Component resolution

Search and inspect exact records for:

- Wearable speaker.
- Slide switch.
- Battery connector.
- MOSFET or transistor.
- Protected LiPo battery.

Do not substitute generic headers for the named XIAO board, speaker, amplifier module, or other named assemblies. Keep unavailable or unresolved parts explicitly documented.

## Firmware

Implement maintainable ESP32-S3 firmware with:

- Separate recording and upload FreeRTOS tasks.
- Bounded queues or double buffers.
- 15-second WAV/PCM chunks stored on FAT microSD.
- Atomic file finalization and recovery scanning after power loss.
- Offline recording and bounded upload retries.
- Wi-Fi provisioning and reconnection.
- TLS API communication with credentials outside source control.
- Camera capture and image-upload support.
- Voice-question and text-to-speech response pipeline.
- Configurable assistant name, personality, language, and wake interaction.
- Optional Home Assistant REST or MQTT integration.
- Provider abstraction for ElevenLabs/OpenAI-compatible services.

## Backend and dashboard contract

Document or scaffold authenticated endpoints for:

- Live transcription.
- Recordings and chunk status.
- Topics, decisions, and action items.
- Meeting summaries.
- Meeting question answering.
- Image descriptions.
- Device state and configuration.

Prefer a persistent live-transcription transport over polling-only behavior. Keep provider credentials server-side and document authentication, retention, consent, and privacy responsibilities.

## Mechanical design

Create a parameterized enclosure with:

- Camera aperture.
- Microphone opening.
- Speaker grille.
- USB-C and microSD service access.
- Power switch and recording-button access.
- Magnetic clothing attachment.
- PCB standoffs and insertion/removal clearance.
- Battery cavity based on the 500 mAh placeholder envelope.

Mark battery, speaker, wall thickness, magnet, connector, and enclosure dimensions as assumptions until exact parts are selected.

## Refactor plan — current product direction

- Retain the XIAO ESP32S3 Sense camera, microphone, and microSD expansion. Add a physical opaque camera privacy shutter with a positive closed position; the camera must be coverable without obstructing the microphone, antenna, USB-C, or microSD access.
- Place the XIAO at the bottom of the enclosure so its onboard USB-C connector is accessible from the enclosure bottom for charging and service.
- Preserve the XIAO's onboard single-cell LiPo charging/power-management path; do not add a separate charger to the BOM unless later measurements show it is required.
- Add two small RGB LEDs to the future design: LED1 for battery/power state and LED2 for recording state. Drive them at low PWM current with per-channel resistors.
- Place LED1 and LED2 at the PCB edge, aligned with small enclosure light ports/light-pipe recesses. The LED package should sit close to, or have its side optically coupled to, the enclosure wall so users can see a subtle color indication externally without exposing the full LED or cutting a large opening.
- Design the openings as narrow, protected apertures or translucent light-pipe windows with a sealed/recessed appearance; prevent direct finger access, accidental snagging, light leakage into the enclosure, and interference with the antenna, shutter, buttons, speaker, or pendant attachment loop. Validate LED visibility at low PWM current from normal viewing angles.
- Use the Bosch BMI270 as the selected future motion sensor candidate, sourced from the [DigiKey India listing](https://www.digikey.in/en/products/detail/bosch-sensortec/BMI270/9974486), subject to final package/land-pattern and availability verification.
- Use the [Robu flat 1027 vibration motor](https://robu.in/product/flat-1027-mobile-phone-vibration-motor/) as the selected haptic-motor candidate. Treat its voltage/current and mechanical envelope as inputs to the driver and enclosure design; do not connect it directly to an ESP32 GPIO.
- Use the bare Analog Devices MAX17048G+T10 fuel-gauge IC directly on the redesigned PCB, not a 7Semi breakout. It estimates LiPo state of charge and reports battery voltage/percentage over I2C; it is not a charger, protection circuit, voltage regulator, or battery. Include the datasheet-recommended support components, I2C address/configuration review, and local layout/decoupling requirements in the PCB redesign.
- Redesign the enclosure with smooth, continuous curves throughout rather than sharp or boxy transitions.
- Integrate the privacy shutter into the smooth enclosure surface, with no exposed sharp edges and no contact pressure on the camera lens when closed.
- Use physical controls only: retain the tactile record button and standby slide switch; do not add capacitive touch controls. An optional second tactile multifunction button may be added later for playback/upload acknowledgement if GPIO and enclosure space permit.
- Prefer tactile/haptic confirmation over touch sensing for record start/stop, privacy actions, low battery, and upload state.
- Design the enclosure with an integrated external attachment loop/eyelet so the product functions as both a wearable pendant and a keychain/accessory. The loop must accept a thread, lanyard, split ring, carabiner, or similar hook without obstructing the camera, shutter, microphone, speaker, USB-C, microSD, controls, or antenna.
- Treat the loop as a load-bearing mechanical feature: use generous rounded transitions and fillets, sufficient wall thickness, a smooth through-hole with no sharp edges, and reinforcement tied into the enclosure body rather than a thin unsupported tab. Validate pull, twist, repeated-use, and drop loads with the intended printed/material revision.
- Prefer an external loop located at a corner or top edge with the hole axis accessible from outside. Reserve clearance for the attachment hardware and prevent the loop or attached ring from contacting the camera lens, privacy shutter, buttons, or antenna.
- Reconcile the board outline, battery tray, speaker cavity, USB-C access, antenna clearance, microSD access, and button/switch access around the new bottom-mounted XIAO before PCB routing.
- Mount the XIAO's supplied 2.4 GHz Wi-Fi/Bluetooth flex antenna flat against a plastic inside wall of the pendant using its adhesive backing, with the radiating face toward the enclosure exterior.
- Reserve the antenna's complete footprint and cable bend radius in the enclosure; keep it away from the LiPo battery, PCB copper/ground, speaker magnet, and any metalized or conductive material. Maintain a preferably 3–5 mm air gap from internal electronics and do not crease or sharply bend the antenna.
- Use this enclosure stack-up as the starting mechanical layout: outer plastic shell, adhesive-backed antenna on a clear side/upper wall, air gap, then PCB/battery/speaker volumes. Confirm final Wi-Fi/Bluetooth range after the enclosure is assembled.

## Local component datasheet and STEP references

The repository source register below is the reference set for the current BOM. Datasheets are stored under [`docs/datasheets/`](datasheets/), and sourced CAD is stored under [`mechanical/components/`](../mechanical/components/). Repeated BOM references intentionally share one retained CAD asset; no duplicate component models are to be added. The existing STEP files are sourced downloads and were file-validated; no CAD geometry was authored during this research pass.

| BOM reference | Local datasheet reference | Local STEP reference | Planning status |
|---|---|---|---|
| U1 — Seeed XIAO ESP32S3 Sense, 113991115 | [`seeed-xiao-esp32s3-sense-113991115.pdf`](datasheets/seeed-xiao-esp32s3-sense-113991115.pdf) | [`seeed-xiao-esp32s3-sense-113991115.step`](../mechanical/components/seeed-xiao-esp32s3-sense-113991115/seeed-xiao-esp32s3-sense-113991115.step) | Sourced and validated |
| U2 — MAX98357AETE+T | [`max98357a-max98357b.pdf`](datasheets/max98357a-max98357b.pdf) | [`max98357aete-t-tqfn-16-3x3mm.step`](../mechanical/components/max98357aete-t/max98357aete-t-tqfn-16-3x3mm.step) | Generic exact TQFN package; sourced and validated |
| U3 — MAX17048G+T10 | [`max17048-max17049.pdf`](datasheets/max17048-max17049.pdf) | [`max17048g-t10-dfn-8-2x2mm.step`](../mechanical/components/max17048g-t10/max17048g-t10-dfn-8-2x2mm.step) | Generic exact DFN package; sourced and validated |
| U4 — Bosch BMI270 | [`bmi270.pdf`](datasheets/bmi270.pdf) | [`bosch-bmi270-lga-14-3x2.5mm.step`](../mechanical/components/bosch-bmi270/bosch-bmi270-lga-14-3x2.5mm.step) | Generic exact LGA package; sourced and validated |
| SPK1 — Same Sky CMS-16093-078L100 | [`same-sky-cms-16093-078x.pdf`](datasheets/same-sky-cms-16093-078x.pdf) | [`same-sky-cms-16093-078l100.step`](../mechanical/components/same-sky-cms-16093-078l100/same-sky-cms-16093-078l100.step) | Exact manufacturer model; sourced and validated |
| BAT1 — NOVA 603450 LiPo | [`generic-lp603450-1100mah.pdf`](datasheets/generic-lp603450-1100mah.pdf) | — | **STEP model creation required.** Use the 6 × 34 × 50 mm envelope and the exact purchased pack/PCM details as inputs; do not treat the generic datasheet as NOVA-specific. |
| M1 — flat 1027 vibration motor | [`qx-flat-1027.pdf`](datasheets/qx-flat-1027.pdf) | — | **STEP model creation required.** Use the verified 10 × 2.7 mm motor envelope after the exact motor is selected; the current Robu page renders Flat 1034. |
| J1/J3 — JST B2B-PH-K-S | [`jst-ph.pdf`](datasheets/jst-ph.pdf) | [`jst-b2b-ph-k-s.step`](../mechanical/components/jst-b2b-ph-k-s/jst-b2b-ph-k-s.step) | Generic exact PH connector; sourced and validated |
| J2 — JST BM02B-SRSS-TB(LF)(SN) | [`jst-sh-series.pdf`](datasheets/jst-sh-series.pdf) | [`jst-bm02b-srss-tb.step`](../mechanical/components/jst-bm02b-srss-tb/jst-bm02b-srss-tb.step) | Exact-ID library model; sourced and validated |
| SW1 — C&K PTS841GKSMTR-LFS | [`pts841.pdf`](datasheets/pts841.pdf) | — | **STEP model creation required.** Preserve the 3.6 × 3.5 × 1.25 mm side-actuated envelope and exact land-pattern/actuator details. |
| SW2 — C&K JS202011AQN | [`ck-js-series-js202011aqn.pdf`](datasheets/ck-js-series-js202011aqn.pdf) | [`jst-js202011aqn.step`](../mechanical/components/jst-js202011aqn/jst-js202011aqn.step) | Exact-ID library model; sourced and validated |
| C1/C3 — Murata GCM188R71H104KA57J | [`murata-gcm188r71h104ka57j.pdf`](datasheets/murata-gcm188r71h104ka57j.pdf) | [`generic-c-0603-1608metric.step`](../mechanical/components/murata-gcm188r71h104ka57j/generic-c-0603-1608metric.step) | Generic exact 0603 package; sourced and validated |
| C2 — YAGEO CC0805KRX5R8BB106 | [`yageo-cc0805krx5r8bb106.pdf`](datasheets/yageo-cc0805krx5r8bb106.pdf) | [`generic-c-0805-2012metric.step`](../mechanical/components/yageo-cc0805krx5r8bb106/generic-c-0805-2012metric.step) | Generic exact 0805 package; sourced and validated |
| R1/R2/R3/R4/R5/R6/R7/R8 — YAGEO RC0603FR series | [`yageo-rc-series.pdf`](datasheets/yageo-rc-series.pdf) | [`generic-r-0603-1608metric.step`](../mechanical/components/yageo-rc0603fr/generic-r-0603-1608metric.step) | Generic exact 0603 package; sourced and validated |
| LED1/LED2 — Kingbright APGF0607G32B33R23-05 | [`kingbright-apgf0607g32b33r23-05.pdf`](datasheets/kingbright-apgf0607g32b33r23-05.pdf) | [`kingbright-apgf0607g32b33r23-05.step`](../mechanical/components/kingbright-apgf0607g32b33r23-05/kingbright-apgf0607g32b33r23-05.step) | Exact manufacturer family model; sourced and validated |
| Q1 — AO3400A | [`ao3400a.pdf`](datasheets/ao3400a.pdf) | [`generic-sot-23.step`](../mechanical/components/ao3400a/generic-sot-23.step) | Generic exact SOT-23 package; sourced and validated |
| D1 — NSVR0320MW2T1G | [`onsemi-nsvr0320mw2t1g.pdf`](datasheets/onsemi-nsvr0320mw2t1g.pdf) | [`generic-d-sod-323.step`](../mechanical/components/onsemi-nsvr0320mw2t1g/generic-d-sod-323.step) | Generic exact SOD-323 package; sourced and validated |
| M1-HARNESS — pre-terminated JST-PH pigtail | [`sunrom-jst-ph-harness.pdf`](datasheets/sunrom-jst-ph-harness.pdf) | — | No verified cable-assembly STEP; use J3 connector model and document wire/strain relief separately |
| 7Semi MAX17048 breakout, dev-only | [`7semi-max17048-breakout.pdf`](datasheets/7semi-max17048-breakout.pdf) | — | No verified board STEP; bare U3 model is not a breakout-board substitute |
| Hubtronics BMI270 breakout, dev-only | [`bmi270.pdf`](datasheets/bmi270.pdf) | — | IC-only datasheet fallback; no verified board STEP |
| Temporary motor test setup | [`qx-flat-1027.pdf`](datasheets/qx-flat-1027.pdf) | — | Shares the future M1 model; no separate duplicate asset |
| TP3/TP4 and custom mechanical items | N/A | N/A | PCB/custom fabrication features, not sourced components |

BAT1, M1, and SW1 are the three deliberate STEP gaps. Their future models must be created only after the final purchased identities and dimensions are confirmed; until then, the BOM and enclosure plan must retain the unresolved status rather than silently substituting a mismatched part.

## Validation sequence

1. Validate the project manifest and select the firmware target.
2. Synchronize PCB packages and dependencies.
3. Build the Zener source and inspect the exact netlist.
4. Generate the KiCad board.
5. Review placement visually and geometrically, including XIAO Sense stack clearance, antenna keepout, speaker/current-loop layout, battery access, and controls.
   - Confirm the antenna is flat, externally oriented, clear of battery/PCB/speaker/metal, and has adequate cable routing and bend relief.
6. Route only after placement review; preserve valid copper.
7. Run ERC, DRC, and PDK-backed DFM checks.
8. Build firmware for the selected ESP32-S3-compatible environment.
9. Build and inspect the enclosure STEP revision.
   - Verify the antenna wall mount, adhesive surface, clearances, cable path, and complete enclosure stack-up in the STEP review.
10. Export and verify BOM, Gerbers, drills, and placement artifacts from one accepted board revision.

## Manufacturing-readiness limitations

Do not call the design manufacturing-ready until electrical, mechanical, firmware, placement, routing, DRC/DFM, and fabrication-export checks pass. Cloud APIs, image analysis, TTS, Home Assistant behavior, and microphone operation require configured services and physical hardware for runtime validation.
