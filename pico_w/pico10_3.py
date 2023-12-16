import network
import time


ssid = 'Yovela'
password = '12345678'


wlan =network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)
    
max_wait = 10
while max_wait >0:
    status = wlan.status()
    if status < 0 or status >=3:
        break
    max_wait -=1
    print("等待連線")
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError(f"{wlan.status()}連線失敗")

else:
     print("連線成功")
     configure = wlan.ifconfig()
     print(f"ip={configure(0)}")
    
    