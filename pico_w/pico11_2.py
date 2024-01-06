from tools import connect,reconnect
from machine import WDT,Timer,ADC,RTC
import time

     

def alert(date,t:float):
    print('要爆炸了!')
    try:
        response = requests.get(url=f'https://hook.us1.make.com/kjchdot2cl5krg3h3eija935sruj03x7?name=pico&date={date}&temperture={t}')
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("Server有錯誤訊息")
            print(f"status:{wlan.status()}")
            response.close()
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')
    rtc = RTC()
    date_turple = rtc.datetime()
    year = date_turple[0]
    month = date_turple[1]
    day = date_turple[2]
    hour = date_turple[4]
    min = date_turple[5]
    second = date_turple[6]
    date = f"{year}-{month}-{day} {hour}:{min}:{second}"
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 24 and delta >= 60 * 1000:        
        alert(date,temperature)
        start = time.ticks_ms()#重新設定計時的時間
      
      



connect()
start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒
    
time1 = Timer()
time1.init(period=1000,callback=callback1)
   

  