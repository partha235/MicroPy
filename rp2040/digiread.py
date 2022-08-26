from machine import Pin
from utime import sleep_ms
sen=Pin(0,Pin.IN)
while True:
    x=sen.value()
    print(x)
    sleep_ms(100)