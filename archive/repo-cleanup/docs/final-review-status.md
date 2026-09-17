# Final review in progress

Acceptance gates: two-layer carrier; retained exact XIAO Sense, MAX98357A, PH battery and SH speaker connectors; top-side components; 28 x 70 mm R2 carrier, four M2 holes; PA12 enclosure with integrated breakaway-cord attachment. No manufacturing release until electrical, mechanical and export reviews pass.

Fresh initial checks: ERC passes (41 advice), DRC 33 missing connections and 30 warnings, DFM passes. No copper. Auto-routing is withheld pending mechanical allocation and placement acceptance.

J1 moved from (94,120) to (100,129) KiCad mm, rotation 180, to move through-hole tails outside the battery tray (CAD Y +/-22 mm). Source comment reconciled; board backup saved by applyPcbPlacement. Screenshot reviewed: no footprint-envelope collision at new location; speaker seat/mated connector height still needs checking. This is a candidate, not accepted final placement.

Updated review: silkscreen clearance/overlap warnings and R1 pad-rotation mismatch are cleared by fresh DRC. Remaining U1/U2 library mismatch warnings are intentional board-only graphic-layer changes, documented in silkscreen-warning-disposition.json with comparison of pad positions, sizes, shapes, nets and drills against the pre-edit board. Do not regenerate the board to remove these exceptions.

Rear depth increased from 9 to 13 mm. At floor Z=-11, the reserved 6 mm cell envelope reaches Z=-3.85; assembled tails must not extend below Z=-2.5, leaving 1.35 mm static vertical clearance. This is conditional on restrained battery position and verified assembled tail projection, not proof of supplier swelling allowance. Cloud revision rev-11f47cda12a3dc63c7106330bc945c2d2428569f6d48420d5ed7f90a180c18e1 passed cavity/floor checks, four single nonempty valid solids, selected part-pair interference checks, and all through-hole-tail/tray interference checks. Exploded snapshot reviewed; occlusion still limits visual fit inspection.

J2 MP1/MP2 are explicitly optional isolated mechanical-tab nets in its existing wrapper, each on a separate pad. They are not functional signal nets and must remain isolated; no invented connection or copper route between them is authorized.

Remaining gates: speaker/J1 mated height; exact Sense microphone/antenna/USB geometry; battery protected maximum envelope/current limits and retention; switch actuator access; fasteners and print qualification; routing and post-route review. Supplier and physical measurements cannot be replaced with successful CAD builds. Auto-layout remains withheld under the requested mechanical-first gate. Old separate STEP exports are stale after the depth change.