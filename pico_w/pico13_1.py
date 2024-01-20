from machine import Pin


red_led = Pin(15,Pin.OUT)
red_led.value(0)
btn = Pin(14,mode=Pin.PULL_DOWN)
