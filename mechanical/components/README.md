# Sourced component STEP files

This directory contains exactly one retained STEP file per unique component/package identity, downloaded from the sources listed in [the 3D-model manifest](../../docs/3d-models.md). Repeated BOM references intentionally share one asset: J1/J3 share the PH header, C1/C3 share the 0603 capacitor envelope, and the 0603 resistor references share one package model. No geometry was authored, resized, simplified, or generated for this request.

The validation performed on 2026-09-08 was file-level validation: each file is ASCII STEP, contains an `ISO-10303-21` header, terminates with `END-ISO-10303-21`, and contains BREP/closed-shell entities. Package models are marked as generic in the manifest; they are suitable for package-envelope clearance only and do not claim manufacturer-specific molding, pin-one, or lead details unless the source is explicitly identified as exact.

The absence of a file is intentional when an exact or defensible generic source could not be found. In particular, no substitute geometry was added for the battery, Robu 1027 motor, PTS841 switch, harness assembly, or breakout boards.

The separate files under `mechanical/exports/` are enclosure/assembly exports, not duplicate component assets, and are retained as distinct mechanical revisions.
