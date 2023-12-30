from machine import Pin
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