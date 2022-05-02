from machine import Pin
from utime import sleep_ms
#from time import sleep
# for esp3 dev kit
led=Pin(2,Pin.OUT) 
while True:
    led.on()
    sleep_ms(100)
    led.off()
    sleep_ms(100)