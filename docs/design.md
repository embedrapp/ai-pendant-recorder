# AI Second Brain pendant — engineering record

The exact XIAO ESP32S3 Sense (SKU 113991115) provides the ESP32-S3, digital microphone, camera connector, and microSD socket. The local MAX98357AETE+T wrapper provides I2S speaker output with 100 nF and 10 uF bypass capacitors. Firmware separates recording and upload FreeRTOS tasks; 15-second chunk files remain local when Wi-Fi is unavailable.

The microphone is the integrated PDM microphone on U1's Sense expansion board: GPIO41 is PDM data and GPIO42 is PDM clock. It is not a separate PCB footprint. Firmware initializes it through Arduino `I2S` in mono PDM mode at 16 kHz/16-bit.

Open hardware decisions: protected LiPo vendor/MPN and dimensions; exact 8-ohm speaker MPN, diameter, thickness, and acoustic volume; final slide switch and battery mating lead; hard EN power-isolation circuit; PCB outline, magnet, standoffs, and enclosure dimensions. The first concept assumes a protected 3.7 V 500 mAh cell.

The DevKitC-1 firmware target is compatibility-only because the installed target catalog has no exact XIAO target. The current firmware is a buildable scaffold, not a completed cloud protocol implementation.