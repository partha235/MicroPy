from machine import Pin
from utime import sleep_ms
led=Pin(2,Pin.OUT)
led.on()
sleep_ms(200)
led.off()
sleep_ms(200)
