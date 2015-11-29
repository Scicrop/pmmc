#!/bin/bash

ANNOT=$(/usr/bin/python /opt/drone-cam/alt-temp.py)

echo $ANNOT

DATE=$(/bin/date +"%Y-%m-%d_%H%M%S")

if [[ "$ANNOT" == NAN ]]; then
 echo "WAITING"
else
 /usr/bin/raspistill -o /opt/drone-cam/pictures/$DATE.jpg -a "$ANNOT"
fi
