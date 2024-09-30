# Analog Input with the MCP3008 10-bit ADC
from gpiozero import MCP3008
from time import sleep

pot = MCP3008(channel=0, clock_pin=4, miso_pin=5, mosi_pin=6, select_pin=12)

while True:
  print(pot.value)
  sleep(0.1)
