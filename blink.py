from machine import Pin 
from time import sleep_ms
led=Pin(25,Pin.OUT)     # here i had used pi pico which has 25 pin as on-board led.
                        #you have to change it according to your board config
while True:
    led.toggle()
    sleep_ms(150)