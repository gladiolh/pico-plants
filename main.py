import network
import socket
import time
from machine import Pin
import ntptime

# WLAN-Zugangsdaten
SSID = 'DEIN_WIFI_NAME'
PASSWORD = 'DEIN_WIFI_PASSWORT'

# Relais Setup (4 Kanäle)
RELAIS_PINS = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]
for r in RELAIS_PINS:
    r.value(1)  # Alle aus (aktive Low)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("🔌 Verbindung mit WLAN wird aufgebaut...")
    while not wlan.isconnected():
        time.sleep(1)
    print("✅ Verbunden:", wlan.ifconfig())
    return wlan.ifconfig()[0]

def sync_time():
    try:
        ntptime.settime()
        print("🕒 Zeit synchronisiert")
    except Exception as e:
        print("⚠️ Zeit konnte nicht synchronisiert werden:", e)

def get_relay_states():
    return [pin.value() for pin in RELAIS_PINS]

def set_relay(index, state):
    RELAIS_PINS[index].value(state)

def html_page():
    relay_states = get_relay_states()
    html = "<html><head><title>Pflanzensteuerung</title></head><body><h2>Relais Steuerung</h2>"
    for i in range(4):
        status = "AN" if relay_states[i] == 0 else "AUS"
        toggle = "AUS" if relay_states[i] == 0 else "AN"
        html += f"<p>Relais {i+1}: {status} " \
                f"<a href='?relay={i}&action=toggle'><button>Schalte {toggle}</button></a></p>"
    html += "</body></html>"
    return html

def start_web_server(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print(f"🌐 Webserver läuft unter http://{ip}/")

    while True:
        cl, addr = s.accept()
        print("📥 Anfrage von", addr)
        request = cl.recv(1024).decode()

        # Steuerung über URL (z.B. /?relay=0&action=toggle)
        if "GET /?relay=" in request:
            try:
                r_part = request.split("relay=")[1]
                relay_num = int(r_part[0])
                current = RELAIS_PINS[relay_num].value()
                RELAIS_PINS[relay_num].value(1 if current == 0 else 0)
            except:
                pass

        response = html_page()
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

# Hauptstart
ip = connect_wifi()
sync_time()
start_web_server(ip)
