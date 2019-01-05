#!/bin/sh -e
echo none | sudo tee /sys/class/leds/led0/trigger
# this turns off the LED on the PIO zero, change to 0 for other PIs
echo 1 | sudo tee /sys/class/leds/led0/brightness
