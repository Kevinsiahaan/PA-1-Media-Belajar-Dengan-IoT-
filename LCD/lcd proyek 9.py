import lcddriver
import time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        s = (input("masukkan data yang ingin di convert menjadi biner:\n"))
        hasil = (' '.join(format(ord(x), 'b') for x in s))
        print("hasil dari convert", hasil)
        print("Writing to display")
        display.lcd_display_string("hasil", 1) # Write line of text to first line of display
        display.lcd_display_string("hasil dari biner", hasil) # Write line of text to second line of display
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_display_string("I am a display!", 1)  # Refresh the first line of display with a different message
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_clear()                               # Clear the display of any data
        time.sleep(2)                                     # Give time for the message to be read

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()