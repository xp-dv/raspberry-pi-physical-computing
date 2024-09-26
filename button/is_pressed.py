# Is Pressed Attribute
from gpiozero import Button

button = Button(5)

button.wait_for_press()
print(button.is_pressed)
print('Why ya try\'na press me?!')
