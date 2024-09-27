# Motor Control Using Robot Module
from gpiozero import Robot
from time import sleep

robot = Robot((4, 5), (26, 27))

robot.forward()
sleep(5)
robot.forward(0.5)
sleep(5)
robot.reverse()
sleep(5)
robot.right()
sleep(5)
robot.left()
sleep(5)
robot.stop()
