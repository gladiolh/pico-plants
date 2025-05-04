# 🌱 Pico Plants – Automatisches Pflanzenmanagement mit Webinterface

Ein einfaches Projekt auf Basis des Raspberry Pi Pico W zur zeitgesteuerten Pflanzenbewässerung und -beleuchtung – inklusive WLAN-Zugriff und Websteuerung über den Browser.

---

## 🔧 Funktionen

- ⏰ Zeitgesteuerte Steuerung von 4 Relais (z. B. Licht & Pumpe)
- 🌐 Webinterface zur manuellen Steuerung der Relais
- 🌍 NTP-Zeitsynchronisation über Internet
- 🧠 Erweiterbar mit Sensoren (z. B. Bodenfeuchtigkeit)

---

## 🖼️ Schaltplan (GPIO-Pins)

![Wiring Diagram](media/wiring_diagram.png)

| Relais | GPIO |
|--------|------|
| 1      | GP2  |
| 2      | GP3  |
| 3      | GP4  |
| 4      | GP5  |

---

## 📲 Webinterface

Öffne die IP-Adresse des Pico W im Browser nach dem Start. Du kannst dort alle 4 Relais ein- und ausschalten.

---

## 📥 Installation

### 1. Voraussetzungen

- Raspberry Pi Pico W
- MicroPython Flash: [Offizieller Guide] (https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)
- Tools: [Thonny IDE] (https://thonny.org/)

### 2. Dateien auf den Pico kopieren

Lade die folgenden Dateien hoch:
- `boot.py`
- `main.py`

### 3. WLAN konfigurieren

Trage deine WLAN-Daten in `main.py` ein:

```python
SSID = 'DEIN_WIFI_NAME'
PASSWORD = 'DEIN_WIFI_PASSWORT'
