# Freerouting API result — 2026-09-21

This directory contains the isolated routing runs and validation artifacts for
the four-layer `ai_pendant_recorder` board.

## Final constrained result

- Active project board: `../layout/layout.kicad_pcb`
- Validated candidate: `layout.width020-low-via-completed2.kicad_pcb`
- Native KiCad report for the active board: `kicad-drc.active-width020-final.rpt`
- Freerouting session: `e6a65db0-ce1e-44ef-b0da-c55112053f57`
- Final API job: `d00ed956-7dff-4153-ba93-abfb5da57d9c`

The final job was routed fresh from the copper-free DSN with automatic
neckdown disabled, strict DRC enabled, 0.50 mm copper-to-edge clearance,
fanout disabled, and all four copper layers routable. The imported route uses
1,264 track segments, all exactly 0.20 mm wide, and 200 vias, all with 0.30 mm
drills.

Freerouting left two local GND opens at microphone `MK1`. They were completed
with 0.20 mm F.Cu tracks routed around the acoustic NPTH. Native KiCad 10 DRC
on the active board reports:

- 0 errors
- 0 unconnected items
- 107 warnings, all missing-library or library-footprint-mismatch warnings

The active board and validated candidate have identical SHA-256 checksums.

## Recovery and comparison files

- `layout.pre-width-constrained-replacement.kicad_pcb`: the previously active
  board, preserved before installing the final constrained result.
- `layout.input-with-partial-copper.kicad_pcb`: the original source snapshot
  captured before the API routing work.
- `layout.no-neckdown.kicad_pcb`: first all-0.20 mm fresh-routing candidate;
  it retained two GND opens.
- `layout.width020-low-via.kicad_pcb`: final API import before the two GND
  connections were completed.
- Earlier first-pass and strict-run files are retained for comparison only;
  they contain undersized tracks and must not be used as the final board.

The API credential is intentionally not stored in this directory.
