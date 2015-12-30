#!/bin/bash
export TERM=dumb
/usr/bin/touch /tmp/wifi.on
/usr/bin/nohup /usr/bin/python /opt/drone-cam/server.py &
/usr/bin/nohup /usr/bin/watch -n6 /opt/drone-cam/auto-cam.sh &
