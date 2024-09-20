# Traffic Lights Sequence (UK Standard)
from gpiozero import TrafficLights, Button, Buzzer
from time import sleep

lights = TrafficLights(4, 5, 6)
button = Button(27)
buzzer = Buzzer(13)

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
