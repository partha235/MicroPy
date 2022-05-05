from machine import Pin
from time import sleep_ms
buz=Pin(2,Pin.OUT) #buzzer connection
while True:
    buz.value(1)
    sleep_ms(150)
    buz.value(0)
    sleep_ms(100)

