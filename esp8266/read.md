# esp8266
ESP8266 is most commonly used low cost wifi module widely used for IoT projects. As esp8266 support only one analog pin it's not good for common projects. Due to it's budget friendly it was good option for home automation and relay based IoT projects.
### On board led
In esp8266 module the on-board led pin goes to GPIO2, but as like other it was not normally connected to gnd pin. So we have to write LOW or FALSE or 0 to this pin for turn on led. In the case of micropython the led turn on when led.off() command is passed.
