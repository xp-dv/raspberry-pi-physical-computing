# Button Wait for Press and Wait for Release Functions
from gpiozero import Button, LED

button = Button(6)
led = LED(17)

while True:
  led.blink()
  button.wait_for_press()
  led.off()
  button.wait_for_release()
