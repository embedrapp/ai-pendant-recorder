# Component STEP / 3D-model manifest

Checked 2026-09-08 IST. This manifest covers every purchased, development-only, and non-purchasable component called out in [bom.md](bom.md). Local files are sourced downloads only; no STEP geometry was created for this task. There is one retained CAD asset per unique component/package identity; repeated BOM references point to the same retained file.

`PASS` means the local download passed file-level STEP checks: ASCII STEP header and terminator plus BREP/closed-shell entities. It is not a claim that a generic package model reproduces every manufacturer-specific detail. `UNRESOLVED` means no usable source file was found or access was gated; the empty model path is deliberate.

## Local models

| Ref / component | Local STEP file | Match | Validation | Source |
|---|---|---|---|---|
| U1 — Seeed XIAO ESP32S3 Sense, 113991115 | [seeed-xiao-esp32s3-sense-113991115.step](../mechanical/components/seeed-xiao-esp32s3-sense-113991115/seeed-xiao-esp32s3-sense-113991115.step) | Exact manufacturer assembly | PASS | [Seeed 3D-model ZIP](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/res/seeed-studio-xiao-esp32s3-sense-3d_model.zip) |
| U2 — MAX98357AETE+T | [max98357aete-t-tqfn-16-3x3mm.step](../mechanical/components/max98357aete-t/max98357aete-t-tqfn-16-3x3mm.step) | Generic exact TQFN-16 / 3 × 3 mm package | PASS | [KiCad TQFN-16 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Package_DFN_QFN.3dshapes/TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm.step) |
| U3 — MAX17048G+T10 | [max17048g-t10-dfn-8-2x2mm.step](../mechanical/components/max17048g-t10/max17048g-t10-dfn-8-2x2mm.step) | Generic exact 8-DFN / 2 × 2 mm package | PASS | [KiCad DFN-8 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x2mm_P0.5mm_EP0.7x1.3mm.step) |
| U4 — Bosch BMI270 | [bosch-bmi270-lga-14-3x2.5mm.step](../mechanical/components/bosch-bmi270/bosch-bmi270-lga-14-3x2.5mm.step) | Generic exact Bosch LGA-14 / 3 × 2.5 mm package | PASS | [KiCad Bosch LGA-14 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Package_LGA.3dshapes/Bosch_LGA-14_3x2.5mm_P0.5mm.step) |
| SPK1 — Same Sky CMS-16093-078L100 | [same-sky-cms-16093-078l100.step](../mechanical/components/same-sky-cms-16093-078l100/same-sky-cms-16093-078l100.step) | Exact manufacturer model | PASS | [Same Sky model ZIP](https://3dcadfiles.3dexchange.net/step_ap203/205/8076781/Same_Sky_CMS-16093-078L100.zip) |
| J1/J3 — JST B2B-PH-K-S | [jst-b2b-ph-k-s.step](../mechanical/components/jst-b2b-ph-k-s/jst-b2b-ph-k-s.step) | Generic exact PH 2-position / 2.00 mm body | PASS | [KiCad JST PH STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Connector_JST.3dshapes/JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical.step) |
| J2 — JST BM02B-SRSS-TB(LF)(SN) | [jst-bm02b-srss-tb.step](../mechanical/components/jst-bm02b-srss-tb/jst-bm02b-srss-tb.step) | Exact-ID library model; verify plating/termination option | PASS | [KiCad JST SH STEP](https://gitlab.com/kicad/libraries/kicad-packages3D/-/raw/master/Connector_JST.3dshapes/JST_SH_BM02B-SRSS-TB_1x02-1MP_P1.00mm_Vertical.step?ref_type=heads) |
| SW2 — C&K JS202011AQN | [jst-js202011aqn.step](../mechanical/components/jst-js202011aqn/jst-js202011aqn.step) | Exact-ID library model | PASS | [KiCad JS202011AQN STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Button_Switch_THT.3dshapes/SW_CuK_JS202011AQN_DPDT_Angled.step) |
| C1/C3 — Murata GCM188R71H104KA57J | [generic-c-0603-1608metric.step](../mechanical/components/murata-gcm188r71h104ka57j/generic-c-0603-1608metric.step) | Generic exact 0603 / 1608 metric package | PASS | [KiCad C0603 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Capacitor_SMD.3dshapes/C_0603_1608Metric.step) |
| C2 — YAGEO CC0805KRX5R8BB106 | [generic-c-0805-2012metric.step](../mechanical/components/yageo-cc0805krx5r8bb106/generic-c-0805-2012metric.step) | Generic exact 0805 / 2012 metric package | PASS | [KiCad C0805 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Capacitor_SMD.3dshapes/C_0805_2012Metric.step) |
| R1/R2/R3/R4/R5/R6/R7/R8 — YAGEO SMD resistors | [generic-r-0603-1608metric.step](../mechanical/components/yageo-rc0603fr/generic-r-0603-1608metric.step) | Generic exact 0603 / 1608 metric package | PASS | [KiCad R0603 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Resistor_SMD.3dshapes/R_0603_1608Metric.step) |
| LED1/LED2 — Kingbright APGF0607G32B33R23-05 | [kingbright-apgf0607g32b33r23-05.step](../mechanical/components/kingbright-apgf0607g32b33r23-05/kingbright-apgf0607g32b33r23-05.step) | Exact manufacturer family model; suffix geometry must be confirmed | PASS | [Kingbright official STEP](https://www.kingbrightusa.com/images/catalog/3D/STEP/APGF0607.STEP) and [product page](https://www.kingbrightusa.com/product.asp?catalog_name=LED&product_id=APGF0607G32B33R23-05) |
| Q1 — AO3400A | [generic-sot-23.step](../mechanical/components/ao3400a/generic-sot-23.step) | Generic exact SOT-23-3 package | PASS | [KiCad SOT-23 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Package_TO_SOT_SMD.3dshapes/SOT-23.step) |
| D1 — NSVR0320MW2T1G | [generic-d-sod-323.step](../mechanical/components/onsemi-nsvr0320mw2t1g/generic-d-sod-323.step) | Generic exact SOD-323 package | PASS | [KiCad SOD-323 STEP](https://raw.githubusercontent.com/KiCad/kicad-packages3D/master/Diode_SMD.3dshapes/D_SOD-323.step) |

## Unresolved or non-purchasable entries

| Ref / component | Model path | Status and reason |
|---|---|---|
| BAT1 — NOVA 603450, 1100 mAh | — | UNRESOLVED. No exact 603450 STEP or defensible generic exact-ID STEP was found from the [Robu listing](https://robu.in/product/nova-603450-1100mah-3-7v-micro-lipo-battery-pack/) or wider search. The generic 603450 PDF in the datasheet folder is documentation only. |
| M1 — Robu flat 1027 motor | — | UNRESOLVED. The [Robu URL](https://robu.in/product/flat-1027-mobile-phone-vibration-motor/) currently renders Flat 1034 (10 mm × 3.4 mm), not a verified 1027, and exposes no CAD. An exact LCM1027A2445F ECAD listing was found, but no downloadable STEP was obtained, so a different motor model was not substituted. |
| SW1 — C&K PTS841GKSMTR-LFS | — | UNRESOLVED. The [DigiKey CAD page](https://www.digikey.in/en/models/10445315) and manufacturer/aggregator pages did not yield a direct exact STEP. The visually similar PTS645 model was deliberately not used. |
| M1-HARNESS — pre-terminated JST-PH cable | — | UNRESOLVED. No cable-assembly STEP was found for the [Sunrom item/category](https://www.sunrom.com/c/jst-ph-20mm); the J3 connector model above is not a harness substitute. |
| 7Semi MAX17048 breakout | — | UNRESOLVED board-level model. The [IoTCart listing](https://iotcart.in/product/max17048-li-poly-li-ion-fuel-gauge-breakout-board-mini-7semi) exposes no verified 3D download. The bare MAX17048 package model above is not a breakout-board model. |
| Hubtronics BMI270 breakout / ES-12135 | — | UNRESOLVED board-level model. A 7Semi BMI270-board STEP was found, but it is a different manufacturer/board and was not copied as an identity-mismatched substitute. |
| Temporary motor test setup | — | UNRESOLVED; same Robu motor source as M1. |
| TP3/TP4 test pads | N/A | PCB features, not purchased components. |
| Custom shutter, loop, shell, antenna mount, LED ports, battery pocket, speaker cavity/grille, magnets and fasteners | N/A | Custom mechanical items, not components represented by this sourced-part manifest. |

## Rejected CAD candidates

These were checked as possible generic substitutes and intentionally not copied into the repository because their identity or envelope did not match the BOM component:

| Component | Candidate | Why rejected |
|---|---|---|
| BAT1 — 603450 LiPo | Marathon battery STEP | Published bounding box is 48.70 × 45.15 × 82.48 mm, not the 603450 6 × 34 × 50 mm envelope. |
| BAT1 — 603450 LiPo | TinyCircuits ASR00012 / 803040 CAD archive | 40 × 30 × 8 mm and no STEP/STP file; not an exact 603450 substitute. |
| M1 — flat 1027 motor | Precision Microdrives 310-101 STEP | Public STEP is for a 10 × 3.4 mm motor; target class is 10 × 2.7 mm. |
| M1 — flat 1027 motor | Marathon vibration-motor STEP | Published bounding box is 150 × 169 × 295 mm; not a coin-motor envelope. |
| SW1 — PTS841 | C&K PTS645 STEP | Different switch family and geometry; not an exact 3.6 × 3.5 × 1.25 mm PTS841 model. |

The local `mechanical/components/` directory therefore contains 14 source STEP files for the components that could be sourced and validated without inventing geometry. The unresolved entries are part of the manifest so they cannot be mistaken for completed coverage.
