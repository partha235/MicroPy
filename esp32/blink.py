from machine import Pin
from time import sleep

led=Pin(2,Pin.OUT) #in esp32 dev kit Pin 2 has onboard led.

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)