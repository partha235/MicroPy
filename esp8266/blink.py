from machine import Pin
from utime import sleep_ms
led=Pin(2,Pin.OUT)
while True:
    led.value(0)
    sleep_ms(100)
    led.value(1)
    sleep_ms(100)
