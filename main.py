from machine import Pin
from time import sleep_ms
sen=Pin(0,Pin.OUT,Pin.PULL_DOWN)
while True:
    print(sen.value())