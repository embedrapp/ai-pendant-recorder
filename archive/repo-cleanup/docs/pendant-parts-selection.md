# Pendant exact-parts selection — prototype shortlist, not fit release

## Basis and decision

Preserve the 32 x 76 mm plan envelope and camera-free front in the current
`mechanical/pendant.py`. Older README camera-bore descriptions are historical.
The existing tray has a 21 x 35 mm cavity; its nominal 20 x 34 x 4 mm protected
500 mAh cell was never a sourced part. No verified drop-in 500 mAh pack was found.
Keep the 500 mAh objective, but recommend the tray/depth changes below. No CAD,
PCB, firmware, generated BOM or purchased-part package was changed in this pass.

## Exact procurement candidates

| Role | Manufacturer / exact ordering identity | Selection and required change |
|---|---|---|
| Battery, 1 | LiPol Battery Co. Ltd **LP502540**, protected version, factory UL1571 AWG28 50 mm leads | 3.7 V, 500 mAh; product page says 40 x 25 x 5 mm, manufacturer's capacity list says 41 mm long. Use 41 mm only as a preliminary envelope, NOT a guaranteed maximum. Requires wider/longer tray and more rear clearance. Order only after supplier confirms protected finished-pack drawing, tolerances, swelling allowance and current limits. Bare leads; connector not included. |
| Speaker, 1 | Same Sky **CMS-16093-078L100** | Wired variant, 16 x 9 x 3 mm, 8 ohm, 0.7 W nominal / 1 W maximum. Replace circular ring with rectangular rim-supported seat, gasket and separated acoustic back volume. Its 18.36 mm diagonal does NOT fit the current 16.6 mm circular seat. Do not buy the spring-contact `078S` variant. |
| Record button, 1 | C&K / Littelfuse **PTS841GKSMTR LFS** | Side-actuated SMT, 3.6 x 3.5 mm outline, 1.25 mm height; distributor lists 250 gf and 0.20 mm travel. Replace top-actuated PTS645 on PCB and design a captured side plunger with a hard stop. Current side opening Z/XY is not matched to this switch. Exact footprint/drawing still needs onboarding. |
| Standby switch, 1 | C&K **JS202011AQN** | Retain existing exact part for low-current EN/AMP_SD standby only. NOT a whole-device battery disconnect: 0.3 A rating does not cover the unresolved total load. Existing library's recorder-current assumption is not accepted as a system current budget. Verify actuator reach and underside tails. |
| Speaker PCB connector, 1 | JST **BM02B-SRSS-TB(LF)(SN)** | Proposed 1 mm SH, top-entry SMT replacement for J2 PH through-hole header. Avoids solder tails beneath J2 and prevents ordinary mating with the PH battery plug. Full connector/mated-wire envelope still needs drawing verification and PCB change. |
| Speaker cable mating set, 1 | JST **SHR-02V-S-B**, two **SSH-003T-P0.2-H** contacts | Assemble an AWG28 harness with qualified crimps; verify speaker lead gauge before crimping directly, otherwise use insulated splices and strain relief. SH series rating is 1 A with AWG28. Pin 1 speaker +, pin 2 speaker −; neither amplifier output is ground. |
| Battery mating housing, 1 | JST **PHR-2**, two **SPH-002T-P0.5S** contacts | Proposed termination of factory cell leads to existing J1 **B2B-PH-K-S**. Confirm contact wire/insulation range and tooling against PH drawing before assembly. Verify actual polarity with a meter before connection: board pin 1 BAT+, pin 2 BAT−. Never infer polarity from housing or wire color alone. J1 tail clearance remains a blocker. |
| Clothing magnets, 8 | supermagnete **S-04-01-N** | Diameter 4 x 1 mm, N45, nickel plated; four opposed pairs. Nominally compatible with current 4.3 x 1.1/1.15 mm pockets, subject to adhesive and encapsulation allowance. Published ~250 g direct-contact attraction is NOT holding force through shell walls and fabric. Prototype retention before accepting. |

Retain existing Seeed **113991115** XIAO ESP32S3 Sense and
**MAX98357AETE+T** amplifier; no new module selection or stack-fit approval is
implied. Preserve camera-free use. Microphone inlet, Sense stack and antenna/coax
still need exact revision metrology. Do not substitute generic headers for them.

## Fit and electrical gates

1. Request LP502540 finished protected-pack drawing: 40/41 mm length conflict,
   maximum thickness, lead exit, protection-board position and expansion allowance.
   Preliminary tray cavity 26 x 42 mm gives only 0.5 mm nominal clearance per side;
   revise from supplier tolerances, not this allocation alone. Existing tray locator
   lugs at X +/-12.2 conflict with a wider tray and must move. Nominal shell internal
   width is 29 mm before local features; verify all surrounding geometry.
2. Existing rear floor is Z=-5 mm; tray floor top is -4.25 mm. A 5 mm cell would
   extend to +0.75 mm, intersecting the PCB at Z=0. Rear depth must increase or the
   architecture change. A preliminary rear_z=8.5 mm gives cell top -1.25 mm, but
   this is NOT approved swelling, insulation or solder-tail clearance.
3. LP502540 supplier lists charge 0.2–0.5 C (100–250 mA), discharge 0.5–1 C
   (250–500 mA). Confirm maximum continuous/pulse limits and PCM trip behavior.
   Measure recording/Wi-Fi/playback peaks before accepting the pack. Limit playback
   and concurrency if needed; 500 mAh capacity does not establish adequate current.
   Verify XIAO charging current, termination under load and temperature behavior.
   The listed pack has no NTC. Hard battery isolation remains a separate design task.
4. Speaker continuous power must remain within 0.7 W. Equivalent sine voltage is
   sqrt(0.7*8)=2.37 Vrms across the speaker, not to ground. Set amplifier gain and
   a measured firmware output ceiling; do not assume MAX98357 full scale is safe.
   Required acoustic volume and gasket compression are not established.
5. Replace J2 footprint and SW1 package only after exact drawing/pin/land-pattern
   validation. Preserve the current physical board before any source synchronization.
   Battery/SH connector cross-mating prevention does not replace polarity checks.
6. Fasteners are intentionally NOT ordered yet. Current lid screw channels run from
   near PCB height to the front face, so an arbitrary M2x6 screw will not secure
   them. Select exact screw length/thread/head after revised Z stack and boss design;
   qualify PA12 pilot hole, torque and cell separation. Mic gasket, grille mesh,
   adhesive and breakaway tether also remain specification/test-dependent.

## Rejected alternatives

- Adafruit **1578**, protected 500 mAh: approximately 29 x 36 x 4.75 mm.
  Its width consumes the nominal entire 29 mm shell cavity before tray and clearance;
  rejected for the unchanged 32 mm exterior.
- Adafruit **3898**, protected 400 mAh: approximately 36 x 17 x 7.8 mm.
  Narrow, but thicker and below capacity target; not a drop-in fallback.
- LP502030, 250 mAh: lower capacity and listed discharge up to 250 mA; not accepted
  merely because its width is near the placeholder.

## Sources and evidence

Manufacturer/distributor pages read during selection:

- Battery: https://www.lipolbattery.com/Lithium-Ion-Polymer-Battery-LP502540.html
- Conflicting length: https://www.lipolbattery.com/LiPo-Battery-500mAh+.html
- Speaker: https://www.sameskydevices.com/product/audio/speakers/miniature-(10-mm~40-mm)/cms-16093-078l100
- Speaker drawing to validate before CAD: https://www.sameskydevices.com/product/resource/cms-16093-078x.pdf
- Record switch series: https://www.littelfuse.com/products/switches/tactile-switches/pts841
- Exact switch variant: https://www.digikey.com/en/products/detail/c-k/PTS841GKSMTR-LFS/10445315
- SH series: https://www.jst-mfg.com/product/detail_e.php?series=231
- Exact SH header: https://www.jst-mfg.com/product/search_nomen_e.php?nomen=BM02B-SRSS-TB&search=Search
- Magnets: https://www.supermagnete.de/eng/disc-magnets-neodymium/disc-magnet-4mm-1mm_S-04-01-N
- Rejected battery sources: https://www.adafruit.com/product/1578 and https://www.adafruit.com/product/3898

Library searches returned no suitable battery/speaker records (unrelated regulator,
amplifier and MCU results were rejected), nor exact new switch/SH header packages.
JS202011AQN record was inspected; its existing package is reported validated with
pcb 0.3.71-rishabh.2, not freshly validated here. New parts have not been installed
or represented with fabricated placeholder footprints.

Validation here: source/document inspection, manufacturer-page comparison and
nominal envelope arithmetic only. No CAD rebuild, interference analysis, electrical
checks, acoustic/RF/thermal tests, live stock confirmation or hardware fit tests.
This is an actionable exact-part shortlist with explicit acceptance gates, not an
approved complete purchasing BOM or a claim that the existing enclosure fits.