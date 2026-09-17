# Routing candidate — incomplete, not fabrication-ready

Current artifact: `pcb/layout/layout.kicad_pcb`.
Run: `pcb-auto-agent-1789659308875-cfr30w`.
Applied-result SHA256: `39832a89ee4c54f18fb94444c19c3d12d4741af334e46c955041d93f4888a1cf`.

Two-layer routing added 1210 segments and 142 vias. LED_SW and LED_FB were
constrained to F.Cu. All 115 footprint blocks, four outline lines and four
outline arcs are byte-identical to the input. No zones were created.
Input and applied-result backups are retained beside the board.

## Executed review
- Inspected merged, F.Cu and B.Cu screenshots. Numerous open connections remain;
  no ground plane exists, and long perimeter routes need return-path review.
- Fresh ERC passed with 79 advice entries.
- Native DRC: 44 unconnected items plus 163 physical violations (207 errors
  total), and 107 library warnings.
- Physical violations: 142 via drills at 0.0003 mm rather than the configured
  0.3 mm; 17 copper-to-edge violations against the existing 0.5 mm rule;
  three GND tracks cross MK1's acoustic NPTH hole at (85.68,94.5) mm;
  one RUN_ENABLE track misses C43 GND clearance (0.1994 vs 0.2 mm).
- DFM failed with 144 errors. See current `.embedr-board` reports beside board.

## Completion prerequisites
Correct the router/import drill-unit handling and obstacle/edge-rule transfer
before another paid run, or edit the candidate with KiCad's semantic copper
tools. Do not weaken board rules or remove the microphone hole to pass checks.
The agent tools currently expose no semantic manual track/via editor.

Repair via drills with fresh clearance/annular-ring checks; reroute microphone
GND around the acoustic aperture, offending edge tracks and the C43 clearance;
complete the 44 open connections. Review boost hot-loop/feedback topology,
power widths against actual load budgets, ground-plane continuity and return
transitions. Refill zones if added, then repeat layer review, native DRC and DFM.
Do not protect this candidate wholesale with preserve_valid: it is not valid.
Do not regenerate the physical board from source to repair these copper issues.