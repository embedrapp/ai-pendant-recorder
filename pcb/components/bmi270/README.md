# BMI270 private package

Grounding: retained `docs/datasheets/bmi270.pdf`, SHA256
`f68ce3c74f011a80bbe4b0279c4abe9609a71a5dcda75a951381d77112e005fb`,
BST-BMI270-DS000-08, pp135 (pins),137 (I2C),143 (package),145 (lands).
No installable Embedr record found. Upstream asset URLs did not resolve;
local symbol and lands authored from the manufacturer drawing.

14 lands, 0.5 mm pitch, 0.475 × 0.25 mm side pads; inner pad edges
0.925 mm from vertical centreline and 0.675 mm from horizontal centreline.
Pin 1 upper left; 1–4 down left, 5–7 across bottom, 8–11 up right,
12–14 across top right to left. No exposed pad. Courtyard is a design allowance.
Mask/paste use KiCad defaults and need fabrication-profile review.

3.3 V VDD/VDDIO; separate 100 nF bypasses. SDO grounded (0x68), CSB high.
Unused auxiliary and interrupt pins NC, not grounded. Firmware must load Bosch
configuration data and set sensor-to-product axis mapping. Polling does not
provide interrupt-based motion wake. Physical layout is not validated yet.