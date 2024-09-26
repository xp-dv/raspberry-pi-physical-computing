# Traffic Lights Sequence (UK Standard)
from gpiozero import TrafficLights, Button
from time import sleep

lights = TrafficLights(6, 5, 4)
button = Button(26)

lights.green.on()
while True:
  button.wait_for_press()
  lights.green.off()
  lights.amber.on()
  sleep(1)
  lights.amber.off()
  lights.red.on()
  sleep(10)
  lights.amber.on()
  sleep(1)
  lights.green.on()
  lights.amber.off()
  lights.red.off()
