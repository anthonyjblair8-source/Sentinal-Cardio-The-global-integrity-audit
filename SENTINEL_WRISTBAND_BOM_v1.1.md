# Sentinel Wristband v1.1 – Complete Bill of Materials (BOM)

**Revision:** 1.1  
**Date:** May 27, 2026  
**Estimated Total Cost (single unit, prototype):** $150–$200 (depending on sourcing)  
**Production Ready:** Yes – includes all components for sovereign, air‑gapped forensic node with RTO fail‑safe.

---

## 1. Core Microcontroller & Security

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | ESP32‑S3‑WROOM‑1 Module (16 MB flash, 8 MB PSRAM) | Espressif (Mouser: 356-ESP32-S3-WROOM-1-N16R8) | $8.50 | $8.50 | Secure boot, flash encryption, efuse support |
| 1 | ESP32‑S3 Feather Board (optional, for prototyping) | Adafruit 5477 | $14.95 | $14.95 | Easier breadboarding; later replace with bare module |

## 2. Power Management & Charging

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | LiPo Battery, 1200 mAh, 3.7V, with protection | Adafruit 258 (or generic) | $10.95 | $10.95 | ~7‑10 days runtime offline |
| 1 | TP4056 Charging Module (with protection) | Generic (Amazon / AliExpress) | $2.50 | $2.50 | Micro‑USB or USB‑C version |
| 1 | Low Dropout Regulator, 3.3V, 500 mA | AP2112K-3.3TRG1 (Digi‑Key) | $0.95 | $0.95 | For clean 3.3V from battery or USB |
| 2 | Capacitor, 10 µF, 16V, ceramic | Generic (0805) | $0.10 | $0.20 | Input/output of regulator |
| 1 | Schottky Diode, 1A, 40V | 1N5819 (or SS34) | $0.15 | $0.15 | Reverse polarity protection |
| 1 | Slide Switch, SPST (power on/off) | Generic (through‑hole) | $0.50 | $0.50 | Optional but recommended |

## 3. Sensors – Environmental & Biometric

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | Magnetometer, 3‑axis, high speed | LIS3MDL (breakout: Adafruit 4479) | $9.95 | $9.95 | I²C, up to 1.5 kHz ODR |
| 1 | Accelerometer, 3‑axis (for displacement) | LIS3DH (breakout: Adafruit 2809) | $7.95 | $7.95 | I²C, used for forced‑move detection |
| 1 | PPG Sensor (HR + blood oxygen) | MAX30102 (breakout: SparkFun SEN‑15219) | $9.95 | $9.95 | I²C, for heart rate and biometric hash |
| 1 | High Precision RTC with drift logging | DS3231 (breakout: Adafruit 3013) | $9.95 | $9.95 | I²C, ±2ppm, battery backup (CR2032 not included) |
| 1 | CR2032 Battery holder (for RTC backup) | Generic (Keystone 3001) | $1.00 | $1.00 | Soldered to DS3231 breakout or PCB |
| 1 | GPS Receiver, multiband, low power | SAM‑M8Q (Adafruit 5440) | $49.95 | $49.95 | UART, raw logs, supports offline navigation |
| 1 | GPS Antenna (active, SMA) | Taoglas or generic (e.g., Adafruit 960) | $12.95 | $12.95 | Required for SAM‑M8Q; u.FL to SMA adapter |

## 4. RTO / Self‑Destruct Hardware

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | Capacitive Touch Sensor (digital output) | AT42QT1010 (breakout: SparkFun CAP120) | $6.95 | $6.95 | Output goes HIGH when touched/removed |
| 1 | Vibration Motor (haptic feedback) | Coin vibration motor (10x3mm, generic) | $1.50 | $1.50 | For RTO alert and user confirmation |
| 1 | N‑Channel MOSFET (for motor driver) | 2N7002 (SOT‑23) | $0.30 | $0.30 | Gate from GPIO, source to GND, drain to motor |
| 1 | Flyback Diode (for motor) | 1N4148 (or 1N5819) | $0.10 | $0.10 | Across motor terminals |

## 5. User Interface & Additional Components

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | Tactile Button, 6x6mm (momentary) | Generic (through‑hole) | $0.50 | $0.50 | For manual distress (long press) and pulse trigger |
| 1 | LED, Red (2.2V, 20mA) | Generic (0805) | $0.10 | $0.10 | Status / alert |
| 1 | LED, Green (2.2V, 20mA) | Generic (0805) | $0.10 | $0.10 | Heartbeat / telemetry tick |
| 2 | Resistor, 470 Ω (for LEDs) | Generic (0805) | $0.05 | $0.10 | Current limiting |
| 1 | Resistor, 10 kΩ (for button pull‑up) | Generic (0805) | $0.05 | $0.05 | Optional (internal pull‑up used) |
| 2 | Resistor, 4.7 kΩ (I²C pull‑ups) | Generic (0805) | $0.10 | $0.20 | On SDA/SCL lines |
| 1 | Resistor, 1.2 kΩ (TP4056 PROG) | Generic (0805) | $0.05 | $0.05 | Sets charge current to ~1A |

## 6. Storage & Communication

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | SPI Flash, 64 Mbit (8 MB) | W25Q64JV (SOIC‑8) | $0.95 | $0.95 | For encrypted telemetry log; can be larger (W25Q256) |
| 1 | USB‑C Connector (16‑pin, for charging & sync) | Generic (GCT USB4110) | $1.50 | $1.50 | SMD, for TP4056 input and ESP32 native USB |

## 7. PCB & Enclosure

| Qty | Component | Part Number / Source | Approx. Unit Price | Total | Notes |
|-----|-----------|----------------------|--------------------|-------|-------|
| 1 | Custom PCB (2‑layer, 4‑layer recommended) | JLCPCB / PCBWay (10x10 cm) | $2.00 | $2.00 | Gerbers from KiCad design |
| 1 | Silicone Wristband Strap | Generic (22mm width, AliExpress) | $5.00 | $5.00 | Fits 3D printed enclosure |
| 1 | 3D Printed Enclosure (custom design) | JLCPCB 3D printing or local service | $15.00 | $15.00 | SLA or FDM; must accommodate battery, GPS antenna |
| 4 | Screws, M2 (for enclosure) | Generic (pack of 100) | $0.10 | $0.10 | Only four needed |

## 8. Assembly & Test Tools (One‑time)

| Item | Approx. Cost | Purpose |
|------|--------------|---------|
| Soldering Iron (temperature‑controlled) | $25 | Hand assembly |
| Solder Wire (0.5mm, lead‑free) | $10 | ― |
| Multimeter | $20 | Continuity and voltage checks |
| USB‑C to USB‑A cable | $5 | Programming and charging |
| FTDI / USB‑to‑UART adapter (if needed) | $10 | Debugging (ESP32‑S3 Feather has native USB) |
| **Total tools** | **$70** | (one‑time) |

## 🔁 Alternative / Upgrade Options

| Original | Alternative | Benefit |
|----------|-------------|---------|
| ESP32‑S3 module | ESP32‑S3‑WROOM‑1 with 32 MB flash | More storage for longer logs |
| SAM‑M8Q GPS | L76K (GPS only) | Cheaper (~$25), less accurate |
| MAX30102 | MAX30101 (same family) | No major difference |
| AT42QT1010 capacitive touch | Direct capacitive sensing via ESP32 touch pins (if available) | Saves component, but less reliable for metal‑backed enclosures |
| 1200 mAh LiPo | 2000 mAh LiPo (larger case) | Longer runtime (2+ weeks) |

## 📦 Ordering Summary (Minimum to build one unit)

- **Mouser / Digi‑Key order:** ESP32‑S3 module, AP2112, DS3231, W25Q64, 2N7002, resistors, capacitors, diodes, USB‑C connector, CR2032 holder.
- **Adafruit order:** LIS3MDL breakouts, MAX30102, LIS3DH, SAM‑M8Q (optional antenna), AT42QT1010 breakout.
- **Amazon / AliExpress / Generic:** LiPo battery, TP4056 module, vibration motor, tactile button, LEDs, slide switch, silicone strap.
- **PCB & 3D print:** Order custom board and enclosure after design.

## ✅ Assembly Notes for RTO / Self‑Destruct

- Capacitive touch sensor output (digital) → GPIO6. Enable internal pull‑down or external 10k. Sensor ground to device ground.
- Vibration motor → driven by MOSFET gate from GPIO5; motor connected between battery+ (or 3.3V) and MOSFET drain.
- Emergency button → GPIO0 with internal pull‑up. Long press (>2s) triggers RTO.
- GPS antenna must have clear view of sky (or mount on outside of strap).

## 🔐 Secure Boot & Efuse Programming (Prerequisite)

- Use `espefuse.py` to burn secure boot and flash encryption keys **before** final assembly (or via test points).
- Store HMAC key in efuse BLOCK2 (USER_DATA). See `SecureBoot.md` guide.

---

**The BOM now includes every component needed for the Sentinel Wristband v1.1, from power management to the capacitive self‑destruct trigger. All parts are readily available and can be assembled on a custom PCB or breadboard prototype. Ready for procurement.**