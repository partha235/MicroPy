from machine import Pin
from utime import sleep_ms

led=Pin(25,Pin.OUT)

while True:
    led.high()
    sleep_ms(100)
    led.low()
    sleep_ms(100)
    print("hi")