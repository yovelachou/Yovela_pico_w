import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Yovela','12345678')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    
if wlan.isconnected():
    print("連線成功")
else:   
    print("連線失敗")
 