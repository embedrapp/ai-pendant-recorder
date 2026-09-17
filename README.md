# AI pendant recorder

Current hardware: base Seeed XIAO ESP32S3 **113991114**, IM69D130 PDM
microphone, Molex 104031-0811 microSD socket, MAX17048 fuel gauge, BMI270,
regulated haptics and a 25-pixel WS2812C-2020-V1 matrix. No camera or speaker.

## Current sources
- [Electrical source](pcb/ai_pendant_recorder.zen)
- [Procurement BOM](docs/bom.md), [structured BOM](pcb/bom.json)
- [LED behavior and limits](docs/rgb-matrix.md)
- [Current status and pin map](docs/current-design.md)
- [Firmware setup](docs/setup.md)

## Revision boundaries
The preserved PCB and mechanical artifacts are not a released implementation
of the current electrical revision. Do not manufacture from historical exports
or regenerate the routed PCB merely to refresh metadata.

Historical component packages, board-edit scripts and superseded documents are
in [archive/repo-cleanup](archive/repo-cleanup). Prior archives remain intact.
Archived files are evidence, not active instructions or current validation.
Mechanical generators and their dependencies remain in place to avoid breaking
existing assemblies; their historical component references do not define the BOM.

Purchase links are user-confirmed in stock, not live numeric inventory. Exact
motor/card/acoustic procurement, electrical/physical checks and bench validation
remain open. BOM completion is not manufacturing release.