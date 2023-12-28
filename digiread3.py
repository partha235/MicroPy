"""this program is to demonstrate the pin with internal "Pullup" & "pulldown" resistor value. 
it increase the accuracy of sensor read value."""
from machine import Pin
from utime import sleep_ms  

sen=Pin(4,Pin.IN,Pin.PULL_UP)     # use when sensor output is "LOW" by default.
sen2=Pin(2,Pin.IN,Pin.PULL_DOWN)  # use when sensor output is "HIGH" by default.
def sen_read():
    global x,y      # declaring the variables as global.
    x=sen.value()   # to read a value of Pin.
    y=sen2.value()
    return x,y        

while True:
    sen_read()
    print(x,"x vale")
    print(y,"y value")
    sleep_ms(100)