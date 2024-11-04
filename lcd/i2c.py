# Printing to a 16x2 LCD Text Display Using I2C
from rpi_lcd import LCD
import time

# Connect VCC to 5V, GND to GND, SDA to SDA, and SCL to SCL

# LCD(address=0x27, bus=1, width=20, rows=4, backlight=True)
lcd = LCD()

#* Print Line
# .text(text, line, align='left')
lcd.text("Hello World!", 1)
lcd.text("<<<", 2, 'right')
lcd.text(">>>", 3)
lcd.text("12345678901234567890", 4)
time.sleep(10)

#* Line Breaking / Word Wrapping
# Words extending past the line width are moved to the next line, not broken up.
# Whitespace is removed when jumping to the next line
# Therefore, this:
message = "This is a quite long sentence that will certainly exceed the first line."
# Becomes this:
  # |----Line Width----|
  # This is a quite long
  # sentence that will
  # certainly exceed the
  # first line.
  # |----Line Width----|

lcd.text(message, 1)
time.sleep(10)

lcd.clear()
