from machine import Pin
from utime import sleep_ms

led=Pin(25,Pin.OUT)

while True:
    led.on()
    sleep_ms(100)
    led.off()
    sleep_ms(100)
    print("hi")