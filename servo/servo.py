# Servo Module PWM Control
from gpiozero import Servo
from time import sleep

# GPIO pin for the servo
SERVO_PIN = 25

# Max and min pulse width
CALIBRATION = -15 # us
min_pw = (500 + CALIBRATION) / 1000000
max_pw = (2500 + CALIBRATION) / 1000000

# Initialize the servo with adjusted pulse width range
servo = Servo(SERVO_PIN, min_pulse_width=min_pw, max_pulse_width=max_pw)

# Move servo to middle position
servo.mid()
print("mid")
sleep(3)

# Move servo to minimum position
servo.min()
print("min")
sleep(3)

# Move servo to middle position
servo.mid()
print("mid")
sleep(3)

# Move servo to maximum position
servo.max()
print("max")
sleep(3)
