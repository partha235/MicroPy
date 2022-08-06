from machine import Pin
from utime import sleep_ms

sen=Pin(4,Pin.IN)
led=Pin(2,Pin.OUT)

while True:
    led.value(sen.value())
    sleep_ms(100)