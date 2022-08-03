from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)
def sen_read():
    global x      
    x=sen.value() 
    sleep_ms(100)
    return x      

while True:
    sen_read()
    print(x)
    if x==1:
        print("saga")
        sleep_ms(250)
    