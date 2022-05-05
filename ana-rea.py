""" this code works with pi pico board which has rp2040 microcontroller in it.
for other board refer another code."""
from machine import Pin,ADC
pot=ADC(26) # refer the pin according to your board config.
while True:
    print(pot.read_u16())