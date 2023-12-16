from machine import ADC,Timer

def callback1(t:Timer):
    temperature = ADC(4)
    vol = temperature.read_u16() *( 3.3/65535)
    print(vol)
    
time1 = Timer()
time1.init(period=1000,callback=callback1)