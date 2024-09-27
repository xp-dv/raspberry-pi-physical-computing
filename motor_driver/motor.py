# Motor Control Using Motor Module
from gpiozero import Motor
from time import sleep

motor1 = Motor(4, 5)
motor2 = Motor(26, 27)

motor1.forward()
motor2.forward(0.5)
sleep(5)
motor1.reverse()
motor2.reverse()
sleep(5)
motor1.stop()
motor2.stop()
