# Value Attribute for Photoresistors
# ! As of Sep 2024, the LightSensor module of gpiozero does not function. Bug status can be found on GitHub
from gpiozero import LightSensor

ldr = LightSensor(6)

while True:
  print(ldr.value)
