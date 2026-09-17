# Electronics workspace

Primary source: `ai_pendant_recorder.zen`. Sourcing is stored in its
`PURCHASE_LINKS`/`DATASHEET_INDEX` maps and the persisted `bom.json` overlay.
`bom.csv` is generated; do not hand-edit it.

`pts841-fixture.zen` is a retained switch fixture. Its JST-SH package remains
required by that fixture even though it is not in the pendant BOM.

`layout/`, `layout-base/`, fixture layouts and `backups/` are preserved artifacts;
no cleanup operation moves copper or establishes physical readiness. Archived
packages/scripts are under `../archive/repo-cleanup/pcb/` and are historical.