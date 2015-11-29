#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO
import time
import os.path
from subprocess import call

butPin = 17 
ledPin = 18 
upBoard = 23

sensor = BMP085.BMP085()

GPIO.setmode(GPIO.BCM) 
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)
GPIO.setup(upBoard, GPIO.OUT)

iface = 'wlan5'
fname = '/tmp/wifi.on'
i=0

def enableCheckWifi(fname):

        if os.path.isfile(fname):
                return
        else:
                call(["ifup", iface])
                f = open(fname,"w")
                f.write("on")
                f.close()
		GPIO.output(upBoard, GPIO.HIGH)
                return

def disableCheckWifi(fname):
        if os.path.isfile(fname):
                call(["ifdown", iface])
                os.remove(fname)
                GPIO.output(upBoard, GPIO.LOW)
		return
        else:
                return



if GPIO.input(butPin):
	while i < 5:
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.50)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(0.50)
		i = i+1
	enableCheckWifi(fname)
	print 'NAN'

else:
	b =  '{0:0.2f}'.format(sensor.read_temperature())
	a =  '_{0:0.2f}'.format(sensor.read_altitude())
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(0.100)
	disableCheckWifi(fname)
	print '\'' +  b+a +'\''


