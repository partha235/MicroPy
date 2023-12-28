# this program simply turn on and off once at it is not on a loop.
from machine import Pin
from utime import sleep_ms
led=Pin(2,Pin.OUT)
led.on()   # check your microcontroller support on() commend or not by running dir(pin)
sleep_ms(200)
led.off()
sleep_ms(200)
