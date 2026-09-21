# Central 5x5 RGB matrix

The speaker-output chain is removed. The board now has a square 5x5 matrix of
25 Worldsemi `WS2812C-2020-V1` addressable RGB LEDs, intended for the visual
thinking/orbit animations in the supplied reference image.

## Electrical implementation

- LED1–LED25 form one 800 kbit/s GRB daisy chain. XIAO D3/GPIO4 drives the
  first pixel through R28 (470 ohm).
- U5 TPS61023 boosts protected `VBAT` to `BOOST_5V` using the TI reference values:
  L1 1 uH, R25 732k, R26 100k, C12 10 uF input, C13/C14 22 uF output.
  The divider gives 4.95 V at the 595 mV typical FB reference
  (`0.595*(1+732/100)`), approximately 4.83–5.08 V across the datasheet's
  580–610 mV PWM reference limits before resistor tolerance. This remains
  inside the LED's documented 3.7–5.3 V operating range.
- U7 TPS22918DBVR switches `BOOST_5V` to the pixel `LED_5V` rail. Its ON pin
  shares XIAO D2/GPIO3 with U5 EN, R27 holds both off through reset, C40=1 nF
  C0G sets about 2.9 ms nominal 5 V rise time, and QOD is tied to `LED_5V` for
  defined discharge. C13/C14 remain on the boost side; per-pixel bypass is on
  the switched side. Firmware holds DATA low before enabling the rail.
- Each pixel has a local 100 nF 0402 capacitor (C15–C39), as required by the
  Worldsemi typical application.

The exact LED is the low-current 5 mA/channel `WS2812C-2020-V1`, LCSC
`C2976072`. Its documented operating range is 3.7–5.3 V and VIH is at least
2.7 V at 5 V, so the XIAO's 3.3 V GPIO directly satisfies the specified input
threshold. Package pinout is DO1, GND2, DI3, VDD4.

## Power limits

The selected Adafruit 1578 / PKCELL protected 500 mAh pack is limited to 1C,
or 500 mA maximum continuous discharge. A theoretical 25-pixel full-white
frame is 375 mA at 5 V before quiescent and conversion losses, which exceeds
the battery budget once the XIAO, storage, microphone, and motor are included.
Firmware must apply a conservative global brightness/current cap, avoid
full-white frames, and inhibit high LED load during motor start. This is an
acceptance requirement, not yet a bench-verified current limit.

Current firmware uses an Adafruit NeoPixel global brightness cap of 24/255,
lights at most five pixels in the recording pulse and one pixel in the idle
orbit, and keeps the haptic gate low by default. The cap is a conservative
software guard, not a substitute for measuring battery, boost, switch and PCB
temperature at minimum battery voltage and worst-case card-write load.
The confirmed product target is no more than 100 mA on the 5 V LED rail.

## Physical intent

### LED-control implementation update

- Animator alone owns data and rail switching after setup. Storage faults request
  FAULT instead of cutting power concurrently with a transmission.
- Startup holds data low, enables the rail, waits a provisional 10 ms, sends
  black, and waits 2 ms before animation. Shutdown sends black, holds data low,
  waits 2 ms, then removes power; no transmissions occur while powered off.
- The 24/255 cap and one/five-pixel animations remain. Recording output is halved
  conservatively for SD load. LED_INHIBIT/LED_OFF provide a request/acknowledgment
  contract for future motor control; HEAVY_LOAD dims future radio activity.
  Motor and radio activity are not currently implemented.
- Low-battery automatic inhibition is NOT implemented: the fuel-gauge driver and
  measured cutoff/recovery thresholds remain required. Do not invent a voltage
  threshold or treat firmware as enforcing measured 100 mA rail current.
- The schematic now reads as five left-to-right rows, preserving exact chain
  connectivity. Physical layout, copper, and component selection are unchanged.
- The configured firmware target is the Seeed XIAO ESP32S3. The clean firmware
  build passes; hardware behavior still requires bench validation.

Place the LEDs as a geometrically regular 5x5 square at board center, with
uniform pitch and identical orientation. Place each bypass capacitor directly
beside its pixel. Keep U5/L1 and their high-current switching loop outside the
microphone acoustic/clock area. The current board uses a regular 5x5 placement;
verify alignment against the enclosure light guide on the physical prototype.

## Evidence

- WS2812C-2020-V1 indexed datasheet: `ds_f7eaed7171762f8cbf8e`
- TPS61023 indexed datasheet: `ds_c3d679f9c6eab3a775cd`
- TPS22918 indexed datasheet: `ds_61aa790c3c3008f98c5e`
- Adafruit 1578 / PKCELL pack: `ds_dcee32f4e0c985211bc8`
- XEL4030 family: `ds_293e09d408f8109bb968`