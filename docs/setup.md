# Firmware setup

Entry point: `src/main.cpp`; framework: Arduino/PlatformIO.
Environment `esp32-s3` currently selects `esp32dev` with `esp-builtin`, an
incompatible configuration for the actual base XIAO ESP32S3. Correct-target
selection and a successful build are required before flashing. Cleanup does
not authorize a target change.

Use a qualified FAT32 microSD card; microphone is the external carrier PDM
IM69D130, not a Sense expansion microphone. See [pin map](current-design.md).
Network configuration is presently unused. Never commit real credentials.
Bench-test rail droop, charge behavior, SD writes, audio and LED sequencing.