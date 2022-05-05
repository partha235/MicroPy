from machine import Pin
from time import sleep_ms
sen=Pin(8,Pin.IN)
while True:
    print(sen.value())