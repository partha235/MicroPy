# this program is to control led with button. led turn on when switch is pushed. 
from machine import Pin
from utime import sleep_ms

but=Pin(4,Pin.IN,Pin.PULL_DOWN)   # connect one terminal to -ve and another to pin 4.
led=Pin(2,Pin.OUT)

while True:
    led.value(but.value())
    print(but.value())
    sleep_ms(100)