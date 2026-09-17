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

Source-only BOM build passed with 102 components before repository cleanup.
See current tool results for post-cleanup validation; no manufacturing release.