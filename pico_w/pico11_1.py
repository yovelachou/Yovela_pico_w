import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Yovela','12345678')

max_wait= 10

#處理正在連線
while max_wait > 0:
    max_wait -= 1
    status =  wlan.status()
    if status < 0 or status >=3:  # 0,1,2:等待  3:連線成功 -1,-2,-3連線失敗
        break
    print("等待連線")
    time.sleep(1)


#有可能根本沒有連線
if wlan.status() != 3:
    #連線失敗，重新開機
    #wdt = WDT(timeout=2000)
    #wdt.feed()
    raise RuntimeError("連線失敗") #開發可寫這行重RUN即可，當產品化時請用上面註解的寫法，讓產品關機重開
    print("連線成功")
    print(wlan.ifconfig())