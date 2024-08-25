from machine import Pin, SoftI2C, ADC
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# Potentiometer Setup
pot = ADC(Pin(15,Pin.IN,Pin.PULL_DOWN))
# pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)       # Full range: 3.3v
pot.width(ADC.WIDTH_12BIT)     # Set width to 12 bits

# OLED display dimensions
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # Read potentiometer value and convert to percentage
    pot_value = int((pot.read() / 4095) * 100)
    print(f"Raw value: {pot.read()}, Percent: {pot_value}%")

    # Clear the display before updating
    oled.fill(0)

    oled.text('Aldehyde test', 0, 0)
    oled.show()
    
    if(pot_value>=18):
        oled.text(f"good", 60, 20)
        oled.show()
        sleep(10)
        oled.fill(0)
    elif(pot_value>=10):
        oled.text("moderate",60,20)
        oled.show()
        sleep(10)
        oled.fill(0)
    elif(pot_value>=1):
        oled.text("bad",60,20)
        oled.show()
        sleep(10)
        oled.fill(0)
    
    # Display text on the OLED
    oled.show()
    
    # Sleep for a shorter duration to allow more frequent updates
    sleep(0.5)
