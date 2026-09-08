# PTS841GKSMTR LFS — private exact package

Source: uploaded Littelfuse/C&K PTS841 datasheet, page 2,
`ds_6387b39722da309d0fd7`, retained at `docs/datasheets/pts841.pdf`.
Top view: upper left/right 1/2, lower left/right 3/4; 1–2 common,
3–4 common; normally open between groups. Actuator faces +Y.

Land pattern: 5.2 mm outer width, 2.8 mm inner gap => 1.2 mm pad
width and X centers ±2.0 mm. 2.4 mm outer height, 0.6 mm row gap
=> 0.9 mm pad height and Y centers ±0.75 mm. GK has neither pegs
nor ESD terminal: omit optional Ø0.8 holes and terminal 5.
Body is 3.5 mm wide; body depth 2.9 mm with actuator extension
0.7 mm. Overall nominal depth 3.6 mm; height 1.25 ±0.2 mm.

Not a shared-library publication. Requires fixture build and rendered
footprint/symbol review before installation on the pendant board.