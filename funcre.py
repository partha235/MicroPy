from machine import Pin
from utime import sleep_ms

class led:
    def __init__(self,led_1):
        self.led_1=Pin(ledpin,Pin.OUT)

    def led_on(self):
        self.led_1.value(0)

    def led_off(self):
        self.led_1.value(1)

ledpin=2
e=led(ledpin)
e.led_on()
sleep_ms(1000)
e.led_off()
sleep_ms(100)
print(dir(e))