
import network, ubinascii
import secrets

# Wifi connection
def connect_wifi(key):
    if key == "tufts":
        wifi = secrets.tuftsWifi
    station = network.WLAN(network.STA_IF)
    station.active(True)
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print("MAC " + mac)

    station.connect(wifi['ssid'],wifi['pass'])
    while not station.isconnected():
        time.sleep(1)
    print('Connection successful')
    print(station.ifconfig())
