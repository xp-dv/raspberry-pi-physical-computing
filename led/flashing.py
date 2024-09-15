# Flashing an LED
from gpiozero import LED
from time import sleep

led = LED(17)
led.on()

while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)
