#!/bin/bash

readonly serial=/dev/ttyUSB0

# fixed location for home
lat=48.092
lon=11.535

location=$(/home/pi/latlon2celestron.py "${lat}" "${lon}")
if [ ${?} != 0 ]; then exit; fi

stty -F ${serial} 9600

HEX="\\\\x%02X"
unset FORMAT
for i in {1..8}; do
  FORMAT="${FORMAT}${HEX}"
done

hex_text="$(printf "W${FORMAT}" ${location})"

echo "Writing location to HC: '${hex_text}'"
echo -ne "${hex_text}" > ${serial}

