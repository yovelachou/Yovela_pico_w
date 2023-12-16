import network
import time

ssid = 'Yovela'
password = '12345678'

wlan =network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)

while not wlan.isconnected() and wlan.status() >=0:
    print("等待連線...")
    time.sleep(1)
    
print(wlan.ifconfig())      