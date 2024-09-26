# Button Activated Tonal Buzzer with LED Indicator
from gpiozero import TonalBuzzer, Button, LED
from gpiozero.tones import Tone

buzzer = TonalBuzzer(13)
button = Button(26)
led = LED(6)

while True:
  button.wait_for_press()
  led.on()
  buzzer.play(Tone("B3"))

  button.wait_for_release()
  led.off()
  buzzer.stop()
