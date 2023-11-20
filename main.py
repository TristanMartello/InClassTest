#main.py
from secrets import ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, ssid, wifi_password
import time
import simple as mqtt

def sending():
    broker = '10.243.51.89' #change this as needed
    ssid = 'Tufts_Wireless'
    password = ''
    topic_pub = "JordanandShiv" #publishing to this topic 
    #topic_sub = "Pico/listen" #in case 2-way communication, subscribe to the topic that the other device is publishing to
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    print("Connected to WiFi")
    #print(wlan.ifconfig()) #this is supposed to get my IP Address...doesn't work idk

    def whenCalled(topic, msg):
        print((topic.decode(), msg.decode()))

    fred = mqtt.MQTTClient('BoneSend', broker, keepalive=600)
    fred.connect()
    
    sending = (fred.check_msg() + " " + time())
    
    fred.publish(topic_pub, sending)
        print(sending)
        time.sleep(0.01)