#!/usr/bin/python
import time
import os.path
import subprocess 

fname='/tmp/wifi.on'
iface='wlan0'

substring = 'inet addr:192.'


if os.path.isfile(fname):
		p = subprocess.Popen(["ifconfig", iface], stdout=subprocess.PIPE)
		out, err = p.communicate()
		if not substring in out:
			subprocess.call(["ifdown", iface])
			time.sleep(10)
			subprocess.call(["ifup", iface])
