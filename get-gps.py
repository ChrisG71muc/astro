#!/usr/bin/env python

import sys
import time
from gps3 import gps3

gpsd_socket = gps3.GPSDSocket()
gpsd_socket.connect(host='127.0.0.1', port=2947)
gpsd_socket.watch()
data_stream = gps3.DataStream()

def getgps():
   for new_data in gpsd_socket:
       if new_data:
            data_stream.unpack(new_data)
       if data_stream.TPV['mode'] != 'n/a':
            mode = data_stream.TPV['mode']
            latitude = data_stream.TPV['lat']
            longitude = data_stream.TPV['lon']
            time.sleep (2)
            if mode == 3:
                return (latitude, longitude)
                break

def dms(deg):
    m = (abs(deg) - int(abs(deg))) * 60.0
    s = (abs(m) - int(abs(m))) * 60.0
    return (int(deg), int(m), int(s))

def celestron(deg):
    c = dms(deg)
    return "{0:d} {1:d} {2:d} {3:d}".format(abs(c[0]), c[1], c[2], 0 if(c[0] >= 0) else 1)

coordinates = getgps()
print "{0} {1}".format(celestron(coordinates[0]), celestron(coordinates[1]))
