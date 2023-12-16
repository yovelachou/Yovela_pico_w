import time
from machine import Pin
 
led = Pin("LED",Pin.OUT)
led2 = Pin("LED",Pin.OUT)
while True:
    led.high()
    led2.high() 
    print('run')
    time.sleep(3)
    led.low()
    print('not run')
    time.sleep(3)