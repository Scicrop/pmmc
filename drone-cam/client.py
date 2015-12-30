#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os.path
from subprocess import call

ledPin = 18 
downBoard = 24
wBoard = 23
i=0;
ret = 'NAN'

GPIO.setmode(GPIO.BCM) 
GPIO.setup(downBoard, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(wBoard, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)
GPIO.setwarnings(False)

fname='/tmp/wifi.on'
iface='wlan0'

def led(times):
	l = 0;
        while (l < times):
                GPIO.output(ledPin, GPIO.HIGH)
                time.sleep(.3)
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(.3)
		l = l +1

def switchWifi(fname):

        if os.path.isfile(fname):
                call(["ifdown", iface])
                os.remove(fname)
		led(10)
		return
        else:
                call(["ifup", iface])
                f = open(fname,"w")
                f.write("on")
                f.close()
		led(5)
                return

while i < 30:
	if GPIO.input(wBoard):
		switchWifi(fname)
		break
	if GPIO.input(downBoard):
		GPIO.output(ledPin, GPIO.HIGH)
		ret = 'OK'
		time.sleep(1)
		break
	else:
		GPIO.output(ledPin, GPIO.LOW)
	time.sleep(.5)
	i = i+1

led(2)

print ret

GPIO.cleanup()
