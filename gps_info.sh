#!/bin/sh -e

# logger "script start"
# sleep 60
# logger "wakeup"
# cd /home/pi
# logger "calling the python script"
# /usr/bin/python -u /home/pi/gps_info.py -d sh1106
/usr/bin/python -u /home/pi/gps3_info.py
# logger "gps_info done"
