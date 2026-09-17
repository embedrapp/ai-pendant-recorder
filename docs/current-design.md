# Current design status

Use `pcb/ai_pendant_recorder.zen` for connectivity and `pcb/bom.json` for sourcing.
The firmware implements PDM recording to microSD and dim LED animations. Radio
upload, fuel-gauge monitoring and motor activation are not implemented.

| XIAO pin | GPIO | Function |
|---|---:|---|
| D0 | 1 | Motor gate |
| D1 | 2 | Record button |
| D2 | 3 | Boost EN / LED switch ON |
| D3 | 4 | LED data |
| D4 / D5 | 5 / 6 | I2C SDA / SCL |
| D8 / D9 / D10 | 7 / 8 / 9 | SD clock / MISO / MOSI |
| MTCK | 39 | SD CS |
| MTDO | 40 | IMU interrupt |
| MTDI / MTMS | 41 / 42 | PDM data / clock |

SW2 holds reset; it is not battery isolation. Battery: Adafruit 1578 protected
500 mAh 1S, documented 500 mA continuous discharge limit. LED rail target is
100 mA, not hardware current limiting. Brief dim animations must be coordinated
with other loads; the firmware interlock is only partially implemented.

Open gates: correct firmware target/build, charger and regulator validation,
motor selection/start-stall current, low-battery behavior, independent ERC,
schematic label cleanup, new PCB placement/routing/DRC/DFM and enclosure fit.
Historical board checks and mechanical revisions do not close these gates.

Standby source build passes with 115 components. U9 gates only the boost/motor
branch (VBAT_PERIPH); J1, XIAO battery input and fuel gauge remain on VBAT.
This is peripheral gating, not battery/charger isolation. SW2 carries control
current only. USB charging remains connected; USB data operation is not promised
while ESP32 EN is grounded.

The current PCB Edge.Cuts has four lines and four joined 3 mm corner arcs,
extents X=82..118 mm, Y=44..120 mm (36 x 76 mm). See compact-placement.md.
The placement helper does not
resolve these arcs and reports boundary containment unknown; this is not evidence
that the outline is absent. Historical 28 x 70 mm enclosure input is obsolete.
Enclosure fit and switch access still require a mechanical revision, not an
assumption that the existing enclosure fits this larger board.

Latest repair removes explicit net assignment to the bus-switch symbol's NC pin,
moves R30 from (110.5,101.5) to (110.5,100.5) mm, and replaces unresolved board
title variables with literal draft identification. No copper has been routed.
Power-transition/backfeed behavior, current budgets, SW2 physical position labels,
schematic readability and board/source synchronization remain review gates.
See current check results; no routing or manufacturing release.