# Ultrasonic Sensor Distance Attribute
from gpiozero import DistanceSensor

ultrasonic_sensor = DistanceSensor(echo=4, trigger=5)

while True:
  print(ultrasonic_sensor.distance)
