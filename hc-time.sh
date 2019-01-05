#!/bin/bash

readonly serial=/dev/ttyUSB0


function getTime() {
  # temporarily disable the ntp client
  service ntp stop

  # force an immediate time update; with timeout at 30s
  timeout 30 ntpd -gq
  code=$?

  # reenable ntp client
  service ntp start

  # if we couldn't get the time in 30s, give up; NOTE: comment out if you install a RTC module!
  if [ ${code} != 0 ]; then exit; fi
}


function setTime() {
  # set the serial port speed
  stty -F ${serial} 9600

  # get the date in the order the protocol calls for
  dtm="$(date -u '+%_H %_M %_S %_m %_d %_y 0 0')"

  # H is the command char; the following 8 bytes are the date/time
  HEX="\\\\x%02X"
  unset FORMAT
  for i in {1..8}; do FORMAT="${FORMAT}${HEX}"; done
  hex_text="$(printf "H${FORMAT}" ${dtm})"

  echo "Writing time to HC: '${hex_text}' -> '${serial}'"
  echo -ne "${hex_text}" > ${serial}
}

set -e

# getTime
# lets get the correct time with rc.local without giving up.

setTime
/home/pi/led-off.sh
