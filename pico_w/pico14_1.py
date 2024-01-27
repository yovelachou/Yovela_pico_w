from machine import Timer,Pin,ADC
import time



def fun10(t:Timer | None = None):
    print("10秒了")
    led.toggle()
   
def fun500ms(t:Timer):
    print(f'Light:{light.read_u16()}')
    print(f'Read:{vr.read_u16()}')
led = Pin(15,Pin.OUT)
light = ADC(Pin(28))
vr = ADC(Pin(27))

timer10 = Timer(period=10000, mode=Timer.PERIODIC, callback=fun10)
timer100ms = Timer(period=500, mode=Timer.PERIODIC, callback=fun500ms)

fun10()


while True:
    print(light.read_u16())
    time.sleep_ms(500)