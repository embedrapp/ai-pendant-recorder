# Electronics workspace

The maintained electrical source is `ai_pendant_recorder.zen`; the current physical board is `layout/layout.kicad_pcb`.

Sourcing metadata is stored in the source `PURCHASE_LINKS` / `DATASHEET_INDEX` maps and the persisted `bom.json` overlay. `bom.csv` is generated and should not be hand-edited.

## Board

- 36 × 76 mm rounded outline
- four copper layers, modeled at 1.62 mm total thickness
- 115 footprints
- 1,264 track segments and 200 vias
- no zones and no reported airwires

The source `Board(...)` points to `layout`, so there is one active board location. Regenerating or synchronizing a routed PCB is a deliberate board mutation; preserve and compare copper before doing so.

## Current checks

- Source build: pass, 115 components.
- ERC: pass, 79 style advice entries.
- DRC: one IM69D130 acoustic-hole/ground-land clearance error plus footprint-library configuration warnings.
- PDK-backed DFM: pass with no findings.

The microphone geometry follows Infineon's recommended 0.8 mm PCB sound port and surrounding solder-mask-defined ground land. Represent that intended geometry with a local KiCad rule or reviewed footprint change; do not weaken the global hole-clearance rule.

The four-layer stackup is a project model rather than a controlled-impedance fabricator stackup. Review boost current loops, trace widths, return paths, and the absence of copper planes before fabrication.
