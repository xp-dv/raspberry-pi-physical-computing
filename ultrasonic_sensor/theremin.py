# Ultrasonic Sensor Theremin

# The lgpio library is used because gpiozero.DistanceSensor doesn’t provide a
# parameter to configure pulse type (my SparkFun sensor requires falling-edge)
# and RPi.GPIO is not compatible with the Raspberry Pi 5
import lgpio
import time

# Pins
ECHO_PIN = 26 # Echo pin of Ultrasonic Sensor
TRIGGER_PIN = 27 # Trigger pin of Ultrasonic Sensor
BUZZER_PIN = 20  # Pin connected to passive buzzer

# Constants
SPEED_OF_SOUND = 0.343 # mm/us
DISTANCE_MIN = 0.0     # mm
DISTANCE_MAX = 2000.0  # mm
FREQ_MIN = 50          # Hz
FREQ_MAX = 1500        # Hz

# Initialize GPIO handle
h = lgpio.gpiochip_open(4) # Default GPIO chip = 4 for Raspberry Pi 5

# Configure pins
lgpio.gpio_claim_input(h, ECHO_PIN)
lgpio.gpio_claim_output(h, TRIGGER_PIN)
lgpio.gpio_claim_output(h, BUZZER_PIN)
lgpio.tx_pwm(h, BUZZER_PIN, FREQ_MIN, 0) # Initialize buzzer with 0% duty cycle

def measure_distance():
  # Trigger the sensor
  lgpio.gpio_write(h, TRIGGER_PIN, 1)
  time.sleep(0.00005) # 50 us
  lgpio.gpio_write(h, TRIGGER_PIN, 0)

  # Wait for the echo response
  start_time = time.time()
  while lgpio.gpio_read(h, ECHO_PIN) == 1: # start_time stops updating when echo goes low
    start_time = time.time()

  while lgpio.gpio_read(h, ECHO_PIN) == 0: # end_time stops updating when echo returns high
    end_time = time.time()

  # Calculate the distance in mm
  pulse_duration = (end_time - start_time) * 1_000_000 # Convert to us
  distance = (pulse_duration * SPEED_OF_SOUND) / 2 # Divide by 2 to account for round-trip

  return distance

def map_distance_to_frequency(distance, min_dist, max_dist, min_freq, max_freq):
  # Map a distance value to a frequency range
  if distance > max_dist:
    return None

  # else: use the interpolation equation to map the distance to an audible frequency
  return int(min_freq + (max_freq - min_freq) * (distance - min_dist) / (max_dist - min_dist))

try:
  print("Ultrasonic Distance Sensor with Buzzer Modulation")
  while True:
    # Measure distance
    distance = measure_distance()

    # Map distance to frequency
    frequency = map_distance_to_frequency(distance, DISTANCE_MIN, DISTANCE_MAX, FREQ_MIN, FREQ_MAX)
    
    print(f"Distance (mm): {distance:.1f}, Freq (Hz): {frequency}")

    if frequency is None:
      lgpio.tx_pwm(h, BUZZER_PIN, FREQ_MIN, 0) # Turn off the buzzer
    else:
      lgpio.tx_pwm(h, BUZZER_PIN, frequency, 50) # 50% duty cycle

    time.sleep(0.1) # Delay reduces strain on CPU, but is still short enough for smooth transitions

except KeyboardInterrupt:
  print("Exiting program")

finally:
  lgpio.tx_pwm(h, BUZZER_PIN, FREQ_MIN, 0) # Turn off buzzer
  lgpio.gpiochip_close(h) # Clean up
