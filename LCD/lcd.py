# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import lcddriver
import time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
#s = (input("masukkan karakter yang ingin di convert"))                                   # Give time for the message to be read
#data = print(' '.join(format(ord(x), 'b') for x in s))

display = lcddriver.lcd()

# Main body of code
try:
    while True:
        print = ("writing to display")
        display.lcd_display_string("Greetings Human!", 1) # Write line of text to first line of display
        display.lcd_display_string("Demo Pi Guy code", 2) # Write line of text to second line of display
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_display_string("I am a display!", 1)  # Refresh the first line of display with a different message
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_clear()                               # Clear the display of any data
        time.sleep(2)
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

