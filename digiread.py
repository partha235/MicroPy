from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)
def sen_read():
    x=sen.value() # to read a value of Pin.
    print(x)
while True:
    sen_read()
    sleep_ms(100)