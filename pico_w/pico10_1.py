from machine import ADC,Timer
import time
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.

def alert():
    print("要爆炸了!!!")
    
def callback1(t:Timer):
    global start
    counter = 0
    sensor = ADC(4)
    vol = sensor.read_u16() *( 3.3/65535)
    temperature = 27 -(vol-0.706)/0.001721
    print(f"溫度:{temperature}")
    delta = time.ticks_diff(time.ticks_ms(), start) # 計算時間差
    print(delta)
    if temperature >26 and delta >= 60 * 1000: # 每分鐘發警告(若溫度超過26度)
        alert()
        start = time.ticks_ms() #重新計算
        
start = time.ticks_ms() - 60 * 1000 #起始時間先減60秒，以利第一次超標時發通知
     
time1 = Timer()
time1.init(period=1000,callback=callback1)