from machine import Pin
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

while True:    
    btn_detact(btn)
     