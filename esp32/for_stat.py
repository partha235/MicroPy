from machine import Pin,PWM
from utime import sleep_ms
frequency=50000 # 0 to 78125
led=PWM(Pin(15),frequency)
while True:
    led.duty(0)
    sleep_ms(50)
    for duty_cycle in range(500,1024):
        print(duty_cycle)
        led.duty(duty_cycle)  # 0 to 1023 for full working range.
        sleep_ms(200)