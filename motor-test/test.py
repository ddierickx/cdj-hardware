#!/usr/bin/env python

import RPi.GPIO as GPIO
import time as TIME
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

#starting from the left, 'left' resembles 0 degrees,
left = (0.6/20.0) * 100
#middle resembles a 90 degree angle
middle = (1.5/20.0) * 100
#right resembles 180 degrees
right = (2.5/20.0) * 100

p = GPIO.PWM(13, 50)
p.start(left)
TIME.sleep(1)
p.start(right)
TIME.sleep(1)
p.start(middle)
TIME.sleep(1)
p.stop()
GPIO.cleanup()
