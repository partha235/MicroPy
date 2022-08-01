""" as file named main run as default in micropython you can reprogram it"""
from machine import Pin
from time import sleep_ms
sen=Pin(7,Pin.IN)
while True:
    print(sen.value(),"saga")
    sleep_ms(100)