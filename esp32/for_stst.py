from machine import Pin
from time import sleep_ms,sleep

led=Pin(2,Pin.OUT) #in esp32 dev kit Pin 2 has onboard led.
while True:
    for i in range(10):
        print(i)
        led.on()
        sleep_ms(500)
        led.off()
        sleep_ms(500)     