from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)
def sen_read():
    x=sen.value() # to read a value of Pin.
    return x
while True:
    print(sen_read())
    sleep_ms(100)