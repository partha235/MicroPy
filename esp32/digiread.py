from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)
def sen_read():
    x=sen.value()
    return x
while True:
   # x=sen.value()  # to read a value of Pin.
    print(sen_read())
    sleep_ms(100)