from machine import Pin,PWM
from utime import sleep_ms
from sys import exit
frequency=50000 # 0 to 78125 for esp32
led=PWM(Pin(2),frequency)
x=0
while True:
    led.duty(0)
    sleep_ms(100)
    for duty_cycle in range(1024):
        print(x)
        if x>=1023:
            print("over limit")
            exit()
        led.duty(x)  # 0 to 1023 for full working range.
        
        sleep_ms(200)
        x=x+50
    x=0