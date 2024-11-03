# Playing Music on a Passive Buzzer
from gpiozero import TonalBuzzer
from time import sleep

passive_buzzer = TonalBuzzer(25)

def play(song):
  for note, duration in song:
    print(note)  # Print current note on terminal
    passive_buzzer.play(note)  # Play current note on buzzer
    sleep(float(duration))  # Hold note for given duration
  passive_buzzer.stop()  # Stop buzzer after song has finished

# Define the song as a list of notes and their durations
song = [
  ('C#4', 0.2), ('D4' , 0.2), (None, 0.2),
  ('Eb4', 0.2), ('E4' , 0.2), (None, 0.6),
  ('F#4', 0.2), ('G4' , 0.2), (None, 0.6),
  ('Eb4', 0.2), ('E4' , 0.2), (None, 0.2),
  ('F#4', 0.2), ('G4' , 0.2), (None, 0.2),
  ('C4' , 0.2), ('B4' , 0.2), (None, 0.2),
  ('F#4', 0.2), ('G4' , 0.2), (None, 0.2),
  ('B4' , 0.2), ('Bb4', 0.5), (None, 0.6),
  ('A4' , 0.2), ('G4' , 0.2), ('E4', 0.2),
  ('D4' , 0.2), ('E4' , 0.2)]

# Play the song
play(song)
