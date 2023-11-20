#main.py
from secrets import ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY
import time
import wifiLib
import simple as mqtt

host_ip = "0.0.0.0"
host_channel = "haha"
listen_channel = "whoa"

sending = ""

def sending(topic, msg):
    global sending
    sending = (msg.decode() + " " + time())
    
def main():
    wifiLib.connect_wifi("tufts")
    try:
        broker = mqtt.MQTTClient('CarPico', host_ip, keepalive=6000)
        print('Connected')
        broker.connect()
        broker.set_callback(sending)
    except OSError as e:
        print('Failed')
        return
    
    # Subscribe to mqtt channels
    broker.subscribe(host_channel)
    while True:
        if sending != "":
            broker.publish(listen_channel, sending)
    
main()

