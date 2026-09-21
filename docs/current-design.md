# Current design status

The maintained design consists of:

- electrical source: `pcb/ai_pendant_recorder.zen`;
- current four-layer board: `pcb/layout/layout.kicad_pcb`;
- firmware: `src/main.cpp`; and
- enclosure generator: `mechanical/pendant.py`.

## Firmware and pin map

The firmware implements PDM recording to microSD and dim LED animations. Radio upload, fuel-gauge monitoring, and motor activation are not implemented.

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

SW2 holds reset; it is not battery isolation. The battery design target is the protected Adafruit 1578 500 mAh 1S cell, documented with a 500 mA continuous discharge limit. The LED rail target is 100 mA rather than a hardware current limit. Brief dim animations must be coordinated with other loads; the firmware interlock is only partially implemented.

## Fresh validation

Checks were run against the current source and board:

- Zener build: pass, 115 components.
- ERC: pass with 0 errors, 0 warnings, and 79 style advice entries.
- KiCad DRC: 1 error and 115 footprint-library configuration warnings.
- PDK-backed DFM: pass with 0 findings.
- Board connectivity view: 1,264 track segments, 200 vias, and 0 airwires.
- Firmware clean build: pass for `seeed_xiao_esp32s3` / `esp32-s3`.
- Enclosure CAD: build and STEP inspection pass with 16 valid solids; measured bounds are 40 × 87.785 × 18.2 mm including the lanyard loop.

The DRC error is at MK1: the IM69D130's 0.8 mm acoustic opening is 0.21 mm from its surrounding GND land, below the board-wide 0.25 mm hole-clearance rule. Infineon's datasheet recommends the 0.8 mm PCB sound port and the surrounding solder-mask-defined ground land used by the footprint. The board still needs a deliberate footprint-specific KiCad rule or a reviewed footprint adjustment so this intended geometry is represented without a global clearance waiver.

The 115 DRC warnings report footprint libraries unavailable to the isolated KiCad checker. The footprints are embedded in the board and the Zener packages build successfully, so these warnings are configuration provenance warnings rather than reported copper or courtyard violations. They should still be eliminated from a final manufacturing handoff by packaging the library tables with the board export.

## Board and power

The PCB outline spans X=82..118 mm and Y=44..120 mm: 36 × 76 mm with 3 mm rounded corners and four 2.2 mm mounting holes. It is a four-layer board with a 1.62 mm modeled stackup. No copper zones are present, so the routed return paths require engineering review rather than assuming continuous reference planes.

U9 gates only the boost/motor branch (`VBAT_PERIPH`). J1, the XIAO battery input, and the fuel gauge remain on `VBAT`. SW2 carries control current only. USB charging remains connected; USB data operation is not promised while ESP32 EN is grounded.

## Remaining engineering work

- Resolve the microphone hole-clearance DRC rule locally and rerun DRC.
- Review boost hot-loop geometry, power widths, return paths, and four-layer stackup with the selected fabricator.
- Validate charger/regulator behavior, backfeed and power transitions on the bench.
- Select and verify the exact motor, including start/stall current and harness.
- Implement and test low-battery behavior, fuel-gauge monitoring, and haptics.
- Verify battery, USB, switch, connector, antenna, cable, and component-height clearances in a physical enclosure prototype.
- Perform audio, SD-write, thermal, charging, LED sequencing, and runtime recovery tests on assembled hardware.
