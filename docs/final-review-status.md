# Final review in progress

Acceptance gates: two-layer carrier; retained exact XIAO Sense, MAX98357A, PH battery and SH speaker connectors; top-side components; 28 x 70 mm R2 carrier, four M2 holes; PA12 enclosure with integrated breakaway-cord attachment. No manufacturing release until electrical, mechanical and export reviews pass.

Fresh initial checks: ERC passes (41 advice), DRC 33 missing connections and 30 warnings, DFM passes. No copper. Auto-routing is withheld pending mechanical allocation and placement acceptance.

J1 moved from (94,120) to (100,129) KiCad mm, rotation 180, to move through-hole tails outside the battery tray (CAD Y +/-22 mm). Source comment reconciled; board backup saved by applyPcbPlacement. Screenshot reviewed: no footprint-envelope collision at new location; speaker seat/mated connector height still needs checking. This is a candidate, not accepted final placement.

Remaining gates: SW2 underside tails over cell; speaker/J1 mated height; exact Sense microphone/antenna/USB geometry; battery protected maximum envelope and current limits; switch actuator access; fasteners and print qualification; silkscreen and R1 footprint mismatch; routing and post-route review. Supplier and physical measurements cannot be replaced with successful CAD builds.