# Momentary Switch Using When Pressed and When Released Functions
from gpiozero import Button, LED
from signal import pause

button = Button(6)
led = LED(17)

button.when_pressed = led.on
button.when_released = led.off
pause()
