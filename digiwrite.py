# this program is  for pi pico
from machine import Pin
from utime import sleep_ms

led=Pin("LED",Pin.OUT)

while True:
    led.high()
    sleep_ms(100)
    led.low()
    sleep_ms(100)
    print("hi")