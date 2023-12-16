import time
from machine import Pin
 
led = Pin("LED",Pin.OUT)
 
while True:
    print('run')
    time.sleep(1)
    print('not run')
    time.sleep(1)