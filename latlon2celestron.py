#!/usr/bin/env python

import sys

lat = float(sys.argv[1])
lon = float(sys.argv[2])

def dms(deg):
    m = (abs(deg) - int(abs(deg))) * 60.0
    s = (abs(m) - int(abs(m))) * 60.0
    return (int(deg), int(m), int(s))

def celestron(deg):
    c = dms(deg)
    return "{0:d} {1:d} {2:d} {3:d}".format(abs(c[0]), c[1], c[2], 0 if(c[0] >= 0) else 1)

print "{0} {1}".format(celestron(lat), celestron(lon))

