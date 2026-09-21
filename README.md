# AI Pendant Recorder

An open-source, privacy-first wearable audio recorder built around the Seeed
XIAO ESP32S3. The current design records PDM microphone audio to a removable
microSD card and uses a 5 × 5 RGB matrix for low-power status feedback.

> [!WARNING]
> This is an active hardware prototype, not a manufacturing release. The
> electrical source is newer than the preserved routed board and enclosure.
> Do not fabricate from the screenshots or historical exports in this repo.

## Hardware at a glance

- Seeed XIAO ESP32S3 **113991114** controller
- Infineon IM69D130 PDM microphone
- Molex 104031-0811 microSD socket
- MAX17048 fuel gauge and BMI270 IMU
- Regulated haptic output
- 25 × WS2812C-2020-V1 RGB LEDs
- Protected 500 mAh 1S LiPo design target
- No camera or speaker

## Schematics

[![Full project schematic](docs/images/schematic.png)](docs/images/schematic.png)

The schematic is generated from
[`pcb/ai_pendant_recorder.zen`](pcb/ai_pendant_recorder.zen). It is organized
into battery/fuel-gauge, controller, motion, microphone, storage, haptics, LED
power, and five LED-row sections. Open the image for the full-resolution view.

## Board

[![Current routed board artifact](docs/images/board-layout.png)](docs/images/board-layout.png)

This image shows the current preserved KiCad board artifact: a 36 × 76 mm
rounded rectangle with four mounting holes. It contains 115 footprints, 1,464
tracks, and no reported airwires in the captured artifact. It is **not** a
released implementation of the latest electrical source; board/source
synchronization, fresh DRC/DFM, and enclosure fit remain open.

## Firmware

The Arduino/PlatformIO firmware currently provides:

- push-to-toggle 16-bit PDM audio capture;
- chunked WAV recording to FAT32 microSD;
- recovery of interrupted `.part` recordings at startup; and
- conservative idle/recording animations on the RGB matrix.

Wi-Fi upload, fuel-gauge monitoring, motor activation, and automatic file
deletion are not implemented.

### Build

1. Install [PlatformIO](https://platformio.org/).
2. Clone this repository and enter it.
3. Build the default environment:

   ```sh
   pio run
   ```

4. Connect a Seeed XIAO ESP32S3 and upload:

   ```sh
   pio run --target upload
   pio device monitor --baud 115200
   ```

Use a qualified FAT32 microSD card. Hardware pin assignments are documented in
[`docs/current-design.md`](docs/current-design.md); additional setup notes are
in [`docs/setup.md`](docs/setup.md).

## Repository map

| Path | Purpose |
|---|---|
| `src/main.cpp` | Recorder firmware entry point |
| `include/` | Shared firmware configuration and WAV helpers |
| `tests/` | Host-side audio-format test |
| `pcb/ai_pendant_recorder.zen` | Authoritative electrical/connectivity source |
| `pcb/layout/` | Preserved KiCad board artifact |
| `pcb/bom.json` | Structured generated BOM |
| `docs/bom.md` | Human-readable procurement notes |
| `mechanical/` | Parametric enclosure work in progress |
| `archives/` | Historical design evidence; not active instructions |

## Project status

The electrical design, PCB artifact, and mechanical assembly are at different
revision boundaries. Before fabrication, the project still needs component and
power validation, board/source reconciliation, independent ERC/DRC/DFM,
physical fit checks, and bench validation. See
[`docs/current-design.md`](docs/current-design.md) for the current engineering
status and known limitations.

## Contributing

Issues and pull requests are welcome. Please keep changes focused, document the
hardware revision they target, and include validation evidence where practical.
Do not commit credentials, private recordings, generated build directories, or
unreviewed manufacturing outputs.

## License

This project is intended to be open source, but no license file is currently
present. Until the maintainers add one, copyright law reserves reuse rights;
please open an issue before redistributing or incorporating the design.