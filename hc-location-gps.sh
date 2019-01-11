#!/bin/bash

readonly serial=/dev/ttyUSB0

location=$(/home/pi/get-gps.py)

if [ ${?} != 0 ]; then exit; fi

stty -F ${serial} 9600

HEX="\\\\x%02X"
unset FORMAT
for i in {1..8}; do
  FORMAT="${FORMAT}${HEX}"
done

echo "Location: '${location}'"
hex_text="$(printf "W${FORMAT}" ${location})"

echo "Writing location to HC: '${hex_text}'"
echo -ne "${hex_text}" > ${serial}
