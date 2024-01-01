""" as file named main run as default in micropython you can reprogram it"""
from machine import Pin,PWM
import time

serv = PWM(Pin(12, mode=Pin.OUT),50)

# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

while True:
    serv.duty(26)
    time.sleep(1)
    print("1st loop")
    serv.duty(123)
    time.sleep(1)