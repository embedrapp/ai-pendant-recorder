# Schematic review against original-plan.md

## Verdict

Architecturally substantially implemented, but **not complete for schematic freeze**.
Basis: current `docs/original-plan.md` (the updated base-XIAO, camera-free plan),
`pcb/ai_pendant_recorder.zen`, its local part wrappers, current runtime build/netlist
summary, schematic capture, and `docs/base-redesign.md`. No circuit or board edits
were made during this review.

## Requirements coverage

| Requirement | Current evidence | Status |
|---|---|---|
| Base XIAO, no Sense/camera | U1 specifies 113991114; external PDM and SD replace expansion; no camera circuit | Present; exact hardware revision/pad access remains a gate |
| USB programming/charging, no external VBUS drive | Uses onboard USB/charger; carrier VBUS and USB data pins deliberately NC | Present in architecture; charger revision/current and operation under load unverified |
| Direct solder, no headers | Whole-board SMD footprint referenced | Physical underside clearance/access not approved |
| High-quality PDM microphone | IM69D130 candidate, SELECT grounded, bypass, 33-ohm clock series resistor and pulldown | Provisional; full manufacturer voltage/timing/pin/land-pattern review open |
| Carrier microSD | DM3D-SF SPI, bypass/bulk, clock series resistor and bus pull-ups | Present; documented land-pattern discrepancy/keepouts unresolved |
| Battery percentage | MAX17048 on shared 3.3 V I2C, bypass; CELL/VDD to VBAT, QSTRT/CTG/grounds grounded | Present; not pack protection or authoritative charger status |
| Motion/context | BMI270, supply bypass, CSB high, SDO low, INT1 to GPIO40 | Present; interrupt wake mode needs confirmation/test; cannot wake MCU while reset held |
| Record/standby, subtle status | Record switch, reset/amplifier standby switch, onboard LED; PCA9685/external RGB removed | Present; standby is not battery isolation or firmware deep sleep |
| Speaker | MAX98357A BTL to J2, bypass, shutdown pulldown/control, gain resistor | Present; selected speaker remains provisional and measured output ceiling required |
| Haptics | Enabled 3.3 V LDO, gate resistor/pulldowns, low-side MOSFET, flyback to motor rail | Present; motor/source start/stall and low-cell dropout performance unverified |
| Protected narrow battery/current budget | Battery connector; pack criteria and provisional peak allowances documented | Not frozen; exact protected pack, pulse rating, charger compatibility and state budget required |
| NTC | No NTC circuit | Conditional, not an omission until documented thermistor pack selected |
| Production access | I2C test pads present | Boot/reset accessibility and practical power/test access not physically reviewed |

GPIO allocation consumes all 15 exposed general-purpose GPIO. GPIO3 amplifier
enable is a boot-strap review item. Microphone/SD have no independent hardware
power switches; low-power operation depends on peripheral modes and firmware.
These limitations must remain explicit, rather than implying full rail gating.

## Fresh validation and limits

- `buildPcbProject`: PASS, 47 components, runtime 0.4.40-embedr.2.
- `inspectPcbNetlist`: PASS, 47 components / 48 nets with expected new component
  IDs and separate MCU/load-side PDM and SD clock nets. This compact tool result
  does not expose all pin memberships: full evaluated pin-by-pin assertions were
  not completed. Wrapper and root-source connections were manually reviewed.
- Schematic capture: seven functional sections present. Long inter-section wires
  and label/power-symbol crowding reduce readability. Small stubs cannot reliably
  be classified from the whole-sheet image; source review is essential.
- `runPcbChecks`: tool-reported ERC PASS, zero errors/warnings, 64 advice, all
  `style.redundant_name`. Advice is cosmetic, not evidence of a disconnected pin.
  Report identifies ERC backend as `zener-pcb-cli`; independent KiCad schematic
  ERC is not established by this result.
- Existing `pcb/layout/layout.kicad_pcb`: DRC FAIL, 115 errors / 32 warnings,
  including clearance and missing connections. DFM reports 10 rules passed and
  5 skipped. Neither result releases the new schematic or board.
- Critically, both that PCB and `pcb/layout/default.net` contain 113991115 and
  PCA9685, and lack IM69D130/DM3D-SF. They are the OLD revision. Source declares
  `layout-base`, while project status resolves the existing `layout` board.
  Preserve the old artifact; establish the new revision deliberately, not by
  treating old exports/checks as current-design evidence.
- Check report: `pcb/layout/.embedr-board/manufacturing-readiness.json`.

## Remaining freeze gates, in order

1. Resolve exact base-XIAO hardware revision, accessible underside pads, pin map,
   regulator budget, boot straps and conflicting 50/110 mA charger evidence.
2. Complete microphone manufacturer datasheet/package review and SD land-pattern
   reconciliation; verify every selected symbol/pad/footprint against its drawing.
3. Select the protected pack and confirm speaker/motor operating limits. Replace
   provisional allowances with a calculated operating-state/peak-current budget;
   define enforceable concurrency/output limits. Bench measurements remain required.
4. Complete fresh evaluated pin-by-pin net assertions and independent ERC for
   the new revision; clean up drawing readability without altering connectivity.
5. Create/reconcile a separately preserved new physical revision, then review
   placement, acoustic/RF/access constraints, routing, DRC and DFM.

Outside schematic scope but relevant to plan acceptance: `embedr.yaml` currently
selects `zeroUSB` / `atmelsam`, not the requested `seeed_xiao_esp32s3`; firmware,
mechanics and several older design/BOM notes are acknowledged stale. No firmware
build, hardware/acoustic/current test, enclosure validation or manufacturing
approval was performed here.