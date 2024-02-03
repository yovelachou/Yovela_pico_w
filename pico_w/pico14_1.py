from machine import Timer,Pin,ADC
import time
from tools import connect,reconnect
import urequests as requests
import dotenv


def fun10(t:Timer | None = None):
    light_value = light.read_u16()
    vr_value = vr.read_u16()
    url = f'https://blynk.cloud/external/api/batch/update?token=d8JG7182JhgWt3s7_vLxWWliHzDmXEKY&V1={vr_value}&V0={light_value}'
    try:
        led.value(1)
        response = requests.get(url)
    except:
        reconnect()
    else:
        if response.status_code == 200:
            print("傳送成功")
        else:
            print("傳送失敗")
        response.close()
    led.value(0)
   
def fun500ms(t:Timer):
    print(f'Light:{light.read_u16()}')
    print(f'vr:{vr.read_u16()}')
    
connect()    
    
led = Pin(15,Pin.OUT)
light = ADC(Pin(28))
vr = ADC(Pin(27))

timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer100ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)

fun10()


while True:
    print(light.read_u16())
    time.sleep_ms(500)