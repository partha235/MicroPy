# This program is for interrupt function that attached to the pin.
# Based on sensor output the trigger mode of irq is alloted.
# For sensor based on active low state "Pin.IRQ_FALLING" is used.
# For sensor based on active high state "Pin.IRQ_RISING" is used


from machine import Pin,enable_irq,disable_irq
from utime  import sleep_ms
sen=Pin(2,Pin.IN,Pin.PULL_DOWN)

def sen_re(pin):
    led=Pin(25,Pin.OUT)
    led.on()
    sleep_ms(100)
    led.off()

while True:
    sen.irq(trigger=Pin.IRQ_RISING,handler=sen_re) 
    print(sen.value())
    sleep_ms(50)