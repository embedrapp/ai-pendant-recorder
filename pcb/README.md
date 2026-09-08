# AI Second Brain pendant PCB Workspace

This sidecar workspace stores native Zener (`.zen`) schematic and PCB sources for the Embedr project.

- Firmware remains managed through `embedr.yaml` and PlatformIO.
- Hardware source-of-truth for schematic and PCB work lives under `pcb/`.
- U1 is the exact Seeed Studio XIAO ESP32S3 Sense, SKU 113991115.
- U2 is the direct MAX98357AETE+T TQFN implementation from the indexed datasheet.
- D1/GPIO2 is the record button; D8/D7/D6 carry I2S BCLK/DIN/LRCLK.
- Build, inspect the netlist, generate the board, then perform placement and DRC review.
