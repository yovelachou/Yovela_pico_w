from machine import Timer

def callback1(t):
    print(1)
    
def callback2(t):
    print(2)


time1 = Timer()
time1.init(freq=1,callback=callback1)

time2 = Timer()
time2.init(period=2000,callback=callback2)




