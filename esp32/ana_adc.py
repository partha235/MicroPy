from machine import Pin,ADC
from utime import sleep_ms

pot=ADC(Pin(25))
pot.atten(ADC.ATTN_11DB) # for 3.3v as full range.
# pot.atten(ADC.ATTN_2_5DB) # for 1.5v as full range.
# pot.atten(ADC.ATTN_6DB)  # for 2v as full range.
# pot.atten(ADC.ATTN_0DB)  # for 1.2v as full range.
pot.width(ADC.WIDTH_12BIT)
while True:
    x=pot.read()
    print(x)
    sleep_ms(100)