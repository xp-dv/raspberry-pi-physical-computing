# Rotary Encoder Rotation and Switch Detection (Polling Method)
from gpiozero import RotaryEncoder, Button
from time import sleep

CLK_PIN = 26
DT_PIN = 27
SWITCH_PIN = 4

encoder = RotaryEncoder(a=CLK_PIN, b=DT_PIN, wrap=True, max_steps=16) # Wrap-around at max 16 steps
encoder_switch = Button(SWITCH_PIN)

last_rotary_value = 0 # Variable to store the last value of rotary encoder
print("Result =", encoder.steps) # Print initial value

try:
  while True: # Infinite loop to continuously monitor the encoder
    current_rotary_value = encoder.steps # Read current step count from rotary encoder

    # Check if the rotary encoder value has changed
    if last_rotary_value != current_rotary_value:
      print("Result =", current_rotary_value) # Print the current value
      last_rotary_value = current_rotary_value # Update the last value

    # Check if the rotary encoder is pressed
    if encoder_switch.is_pressed:
      print("Switch pressed!") # Print message on switch press
      encoder_switch.wait_for_release() # Wait until switch is released

    sleep(0.1) # Short delay to prevent excessive CPU usage

except KeyboardInterrupt:
  print("Program successfully terminated") # Print message when program is terminated via keyboard interrupt
