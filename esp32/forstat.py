from machine import Pin,PWM
from time import sleep_ms
x=Pin(25)
y=PWM(x,1000)

for i in range(0,1024):
    print(i)
    y.duty(i)
    sleep_ms(100)