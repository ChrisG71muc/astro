#!/bin/sh -e
echo mmc0 | sudo tee /sys/class/leds/led0/trigger
