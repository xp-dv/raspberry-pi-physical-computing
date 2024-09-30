# Dimming LEDs Using PWMLED
from gpiozero import PWMLED
from gpiozero import MCP3008 # MCP3008 ADC provides analog input
from time import sleep

led = PWMLED(24)
pot = MCP3008(channel=0, clock_pin=4, miso_pin=5, mosi_pin=6, select_pin=12)

led.on()
sleep(3)
led.off()
sleep(3)
led.value = 0.5 # PWM 50% duty cycle
sleep(3)
led.source = pot.values # Equivalent to: "while True: led.value = pot.value"
sleep(20)
