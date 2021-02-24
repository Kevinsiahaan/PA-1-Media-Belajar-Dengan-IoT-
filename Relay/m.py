#!/usr/bin/python
import RPi.GPIO as GPIO
import time

print("Selamat Datang")
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [17, 27, 22, 10, 9, 11, 0, 5]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.5

# main loop
s = (input("masukkan data yang ingin di convert menjadi biner:\n"))

try:
  GPIO.output(17, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(27, GPIO.HIGH)
  print ("NULL")
  time.sleep(SleepTimeL);
  GPIO.output(22, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(10, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(9, GPIO.HIGH)
  print ("NULL")
  time.sleep(SleepTimeL);
  GPIO.output(11, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(0, GPIO.LOW)
  print ("ONE")
  time.sleep(SleepTimeL);
  GPIO.output(5, GPIO.HIGH)
  print ("NULL")
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
