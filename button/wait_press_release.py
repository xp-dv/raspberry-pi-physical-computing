# Wait for Press and Wait for Release Methods
from gpiozero import Button, LED

button = Button(26)
led = LED(6)

while True:
  led.blink(0.5, 1)
  button.wait_for_press()
  led.off()
  button.wait_for_release()
