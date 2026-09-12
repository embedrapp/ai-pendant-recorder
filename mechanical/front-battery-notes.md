# Front battery / top speaker prototype

## Selected battery

The tray is now designed around **Adafruit product 1578**, a protected 1S
3.7 V, 500 mAh Li-polymer pack. Adafruit listed it in stock at selection time
for USD 7.95, and Fab.to.Lab lists the Adafruit battery family for Indian
ordering. Purchase and local variant availability are not assumed.

The PKCELL datasheet identifies a 500 mAh pack with PCM, 4.2 V CC/CV charge,
and 1C (500 mA) maximum continuous discharge. Adafruit specifies a JST-PH lead,
overcharge/over-discharge/short-circuit protection and no thermistor. The current
PCB J1 is two-pin only (pin 1 VBAT, pin 2 GND), so it cannot monitor an NTC.
Verify connector polarity against J1 before connection.

## Authoritative envelope and tray

The Adafruit page reports 29 x 36 x 4.75 mm. The attached pack drawing reports
30 +/-0.1 x 35 +/-0.1 x 5 +/-0.1 mm. CAD therefore uses the conservative union
**30.1 x 36.0 x 5.1 mm**, including the PCM/taped pack body, and reserves
**30.1 x 36.0 x 6.1 mm** to provide 1.0 mm expansion allowance.

The removable tray has a 30.6 x 36.5 mm rectangular cavity, 0.25 mm nominal
clearance per side, a 32.2 x 38.1 mm floor/rim design, a low non-compressive
locating rim, and a 10 mm lead notch. The 100 mm lead is service-looped; no lead
bend radius or connector body is counted as part of the pouch cavity.

Use a solid insulating floor and battery-compatible pull-release adhesive. Do
not clamp the pouch faces, place sharp solder tails against it, or obstruct the
expansion reserve. PCB placement, shell size and mounting holes remain unchanged.

## Validation and remaining gates

Cloud CAD built the isolated tray as revision
`rev-648ce205ca8252e6307f1d42659a1ad77af3a73062552ee70042cac07e545eed`.
The STEP contains inspectable valid solids and is exported at
`mechanical/exports/pendant-battery-tray-adafruit-1578.step`. The complete
assembly and cutaway also built without asserted tray/battery/lid/shell or
provisional component-envelope interference.

This is a CAD fit prototype, not purchase or production approval. Before use,
confirm the delivered pack dimensions and polarity, charger current/behavior,
PCM protection details, UN38.3/MSDS applicability, India shipping, actual peak
device current, assembled component heights, cable routing, insulation and
thermal/RF clearance. Trial-fit a non-energized sample before charging.