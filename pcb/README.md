# Electronics workspace

Primary source: `ai_pendant_recorder.zen`. Sourcing is stored in its
`PURCHASE_LINKS`/`DATASHEET_INDEX` maps and the persisted `bom.json` overlay.
`bom.csv` is generated; do not hand-edit it.

`pts841-fixture.zen` is a retained switch fixture. Its JST-SH package remains
required by that fixture even though it is not in the pendant BOM.

`layout/`, `layout-base/`, fixture layouts and `backups/` are preserved artifacts;
no cleanup operation moves copper or establishes physical readiness. Archived
packages/scripts are under `../archive/repo-cleanup/pcb/` and are historical.

## Four-layer reroute
User requested removal of all old copper and four-layer routing. Active physical
artifact is `layout/layout.kicad_pcb`; do not regenerate from `layout-base`.
Previous routed board and project rules are saved in `backups/before-four-layer-*`.
Placement, pads, holes and outline are retained. Source layer count is four.
Draft stackup retains 1.62 mm total: four 0.035 mm copper layers, 0.2/1.06/0.2 mm
dielectrics and two 0.01 mm masks. These are provisional CAD defaults, not a
fabricator-approved or controlled-impedance stackup. All four layers are available
for routing; no continuous reference planes are implied. Boost hot-loop/current
capacity and signal returns require review before fabrication.

Reroute run `pcb-auto-agent-1789671229431-uxntw0` returned a partial candidate:
505 segments (440 front, 9 In1, 21 In2, 35 back), 40 vias, 182 open connections.
All four layer screenshots were inspected; inner layers contain sparse traces,
not reference planes. Source build and ERC passed. Fresh checks reported 229 DRC
errors, 107 warnings and 40 DFM errors. Native inspection confirms all 40 imported
via drills are incorrectly 0.0003 mm; router/import conversion needs correction
before another paid attempt. Edge clearance violations also remain. Provider
warned that the MK1-5 keepout was ignored. Do not accept this candidate for manufacture.
Component anchors, rotations, sides, footprint identities and pad nets/drills
match the pre-change board; full pad-coordinate equality was not established.