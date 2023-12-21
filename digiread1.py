from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)

while True:
    x=sen.value() # to read a value of Pin.
    print(x)
    sleep_ms(100)