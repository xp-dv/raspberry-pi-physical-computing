# Toggle Switch Using Wait For Press
from gpiozero import Button, LED
from time import sleep

button = Button(6)
led = LED(17)

while True:
  button.wait_for_press()
  led.toggle()
  sleep(0.5)
