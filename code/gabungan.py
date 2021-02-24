#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pinList = [2,3,4,17,27,22,10,9]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i ,GPIO.HIGH)

s = (input("masukkan data yang ingin di convert menjadi biner:\n"))
hasil = (' '.join(format(ord(x), 'b') for x in s))
print("hasil dari convert:" ,hasil)

array.hasil = [0,1,2,3,4,5];

 if hasil == 1:
     GPIO.output(RELAY1, GPIO.HIGH)
 else :
     GPIO.output(RELAY1, GPIO.LOW)

hasil = [1]
RELAY2 = 3
 if hasil == 1:
    GPIO.output(RELAY2, GPIO.HIGH)
 else:
    GPIO.output(RELAY2, GPIO.LOW)

hasil = [2]
RELAY3 = 4
 if hasil == 1:
    GPIO.output(RELAY3, GPIO.HIGH)
 else:
    GPIO.output(RELAY3, GPIO.LOW)

hasil = [3]
RELAY4 = 17
 if hasil == 1:
    GPIO.output(RELAY4, GPIO.HIGH)
 else:
    GPIO.output(RELAY4, GPIO.LOW)

hasil = [4]
RELAY5 = 27
 if hasil == 1:
    GPIO.output(RELAY5, GPIO.HIGH)
 else:
    GPIO.output(RELAY5, GPIO.LOW)

hasil = [5]
RELAY6 = 22
 if hasil == 1:
    GPIO.output(RELAY6, GPIO.HIGH)
 else:
    GPIO.output(RELAY6, GPIO.LOW)

hasil = [6]
RELAY7 = 10
 if hasil == 1:
    GPIO.output(RELAY7, GPIO.HIGH)
 else:
    GPIO.output(RELAY7, GPIO.LOW)

hasil = [7]
RELAY8 = 9
 if hasil == 1:
    GPIO.output(RELAY8, GPIO.HIGH)
 else:
    GPIO.output(RELAY8, GPIO.LOW)

import i2clcd

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

try:
    print("Writing to display")
    display.lcd_display_string("Hasil", 1) # Write line of text to first line of display
    while True:
        s = (input("masukkan data yang ingin di convert menjadi biner:\n"))
        hasil = (' '.join(format(ord(x), 'b') for x in s))

        display.lcd_display_string(str(hasil), 2) # Write just the time to the display
        # Program then loops with no delay (Can be added with a time.sleep)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
   display.lcd_clear()