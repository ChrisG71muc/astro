#!/usr/bin/env python

import os
import datetime
import time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont
from gps3.agps3threaded import AGPS3mechanism

agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 
datetime.time(15, 8, 24, 78915)

def dms(deg):
    m = (abs(deg) - int(abs(deg))) * 60.0
    s = (abs(m) - int(abs(m))) * 60.0
    return (int(deg), int(m), int(s))

def stats(device):
    # use custom font
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                'fonts', 'ProggyTiny.ttf'))
    font2 = ImageFont.truetype(font_path, 16)
    systimes = format(datetime.datetime.now().time())
    gpstimes = format(agps_thread.data_stream.time)
    lats = format(agps_thread.data_stream.lat)
    lons = format(agps_thread.data_stream.lon)
    alts = format(agps_thread.data_stream.alt)
    gpsmodes = format(agps_thread.data_stream.mode)

    with canvas(device) as draw:
        draw.text((0, 0), systimes, font=font2, fill="white")
        draw.text((0, 14), gpstimes, font=font2, fill="white")
	draw.text((0, 28), "Lat: " + lats, font=font2, fill="white")
        draw.text((0, 42), "Lon: " + lons, font=font2, fill="white")
        draw.text((0, 56), "Alt: " + alts, font=font2, fill="white")
        draw.text((80, 56), "Mode: " + gpsmodes, font=font2, fill="white")


def main():
    while True:
        stats(device)
        time.sleep(1)


if __name__ == "__main__":
    try:
        serial = i2c(port=1, address=0x3C)
        device = sh1106(serial, rotate=2)
        main()
    except KeyboardInterrupt:
        pass
