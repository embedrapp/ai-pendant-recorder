# Routing gate — still open

Reviewed combined front copper/front and back fabrication image. Opposite-side overlaps of U1 with surface-mount R29/R30/Q2 and test pads are not body collisions. J4 card projection and SW2 actuator overhang are intentional; see compact-placement.md for exact insertion direction.

Changes: H3 moved from (85.5,116.5) to (84.9,116.5) mm. Nominal 2.1 mm-radius support ends at X87.0, versus U1 rendered envelope X87.369: 0.369 mm nominal separation, not tolerance-qualified. Rounded board corner and full fastener/tool envelope remain to qualify. C13 moved to (116.2,68), 270 degrees, VOUT pad toward U5 pin 6 and GND toward pin 4, avoiding a wraparound output loop. TI SLVAES4 identifies output capacitor placement as critical. Rendered C13 extent X117.18 leaves 0.82 mm to board edge. No routing added.

Current placement snapshot: current-placement.json. Source directives record local edits; do not regenerate the whole board without reconciling other manual placements.

Blocking evidence still needed: actual external U.FL antenna identity/envelope and cable installation, mated connector and battery lead clearances, full mechanical fit with actual U1 model, missing component heights. XIAO wiki in this directory explicitly specifies an external antenna. No fictional antenna keepout was created. Routing is NOT released by this note. Mechanical generator derives H3 from current board and must be rebuilt; old imported detailed PCB is stale after these changes.