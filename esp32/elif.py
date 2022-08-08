from machine import Pin,ADC
from utime import sleep_ms
pot=ADC(Pin(25))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
while True:
    x=pot.read()
    print(x)
    if x>=4000:
        print("auto pilot")
        sleep_ms(500)
    elif x>=3000:
        print("auto gear")
        sleep_ms(500)
    elif x>=1500:
        print("auto speed control")
        sleep_ms(500)
    elif x>=500:
        print("object detection")
        sleep_ms(500)
    else:
        print("manual")
        sleep_ms(800)