from machine import Pin
from tools import connect,reconnect
import urequests as requests
import time


red_led = Pin(15,Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
led_status = False

def btn_detact(btn1):
    global is_press, led_status
    
    if btn.value():
        time.sleep_ms(50)
        if btn.value():
           is_press = True
    elif is_press:
        time.sleep_ms(50)
        if btn.value() == False:
            print('release')
            led_status = not led_status
            red_led.value(led_status)
            is_press = False
            try:
                if led_status == True:
                    get_url = 'https://blynk.cloud/external/api/update?token=d8JG7182JhgWt3s7_vLxWWliHzDmXEKY&V0=1'
                else:
                     get_url = 'https://blynk.cloud/external/api/update?token=d8JG7182JhgWt3s7_vLxWWliHzDmXEKY&V0=0'
                response = requests.get(get_url)       
            except:
                reconnect()
            else:
                if response.status_code == 200:
                    print("傳送成功")
                else:
                    print("server有錯誤訊息")
                    print(f'status_code:{response.status_code}')
                response.close()
            
connect()   
while True:    
    btn_detact(btn)
     