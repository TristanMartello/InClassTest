
from secrets import ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY
import wifiLib

host_ip = "0.0.0.0"
host_channel = "haha"

def whenCalled(topic, msg):
    print(topic.decode())
    print(msg.decode())

def main():
    wifiLib.connect_wifi("tufts")
    try:
        broker = mqtt.MQTTClient('CarPico', host_ip, keepalive=6000)
        print('Connected')
        broker.connect()
        broker.set_callback(whenCalled)
    except OSError as e:
        print('Failed')
        return
    
    # Subscribe to mqtt channels
    broker.subscribe(host_channel)
    
main()

