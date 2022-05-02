from machine import Pin
from utime import sleep_ms
#from time import sleep
#for pi pico (rp2040)
led=Pin(25,Pin.OUT)
while True:
    led.toggle()
    sleep_ms(100) 