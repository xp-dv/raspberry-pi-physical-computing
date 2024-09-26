# Traffic Lights Blink Method
from gpiozero import TrafficLights, Button

lights = TrafficLights(4, 5, 6)
button = Button(26)

while True:
  lights.blink(0.5, 0.5)
  button.wait_for_press()
  lights.on()
  button.wait_for_release()
  lights.off()
  button.wait_for_press()
  button.wait_for_release()
