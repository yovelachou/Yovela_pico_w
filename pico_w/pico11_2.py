import network
import time
from machine import WDT,Timer,ADC

def connect():
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


    #沒有WIFI的處理
    if wlan.status() != 3:
        #連線失敗，重新開機
        #wdt = WDT(timeout=2000)
        #wdt.feed()
        raise RuntimeError("連線失敗") #開發可寫這行重RUN即可，當產品化時請用上面註解的寫法，讓產品關機重開
    else:
        print("連線成功")
        print(wlan.ifconfig())
        



def alert():
    print('要爆炸了!')
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 24 and delta >= 60 * 1000:        
        alert()
        start = time.ticks_ms()#重新設定計時的時間
        
connect()
start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒
    
time1 = Timer()
time1.init(period=1000,callback=callback1)




  