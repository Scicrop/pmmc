#!/bin/bash
export TERM=dumb
ANNOT=$(/usr/bin/python /opt/drone-cam/client.py)
ECHO $ANNOT
DATE=$(/bin/date +"%Y-%m-%d_%H%M%S")

if [[ "$ANNOT" == NAN ]]; then
 echo "WAITING"
else
 /usr/bin/raspistill -o /opt/drone-cam/pictures/$DATE.jpg
fi
