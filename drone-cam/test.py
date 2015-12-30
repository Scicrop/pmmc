# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
butPin = 17 # Broadcom pin 17 (P1 pin 11)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

if GPIO.input(butPin):
	print 'tada'
