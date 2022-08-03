from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)
def sen_read():
    global x      # declaring the variable as global.
    x=sen.value() # to read a value of Pin.
    return x      # this program is to find difference between "return" & "print".

while True:
    sen_read()
    print(x)
    sleep_ms(100)