#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
left = 11
right = 12
R_Light = 15
L_Light = 22
delay = 4
T1 = 0
T2 = 0
TE = 0
OPEN = "open"
CLOSED = "closed"
Rcounter = 0
Lcounter = 0
door_delay = 3

#check door status
def door_status(x1):
    return OPEN if GPIO.input(x1) else CLOSED

def closeDoor(door):
    GPIO.output(door, True)
    time.sleep(1)
    GPIO.output(door,False)

GPIO.output(R_Light,False)

while True:
    if door_status(right) == OPEN:
        if Rcounter > delay:
            print "Right Door has been open too long, closing..."
            closeDoor(R_Light)
            time.sleep(door_delay)
            print "Door should now be closed"
            Rcounter = 0
        else:
            Rcounter+=1
            print "Right Door has been open ", Rcounter, " second"
    else:
        print "Right Door is closed"
        Rcounter = 0
    if door_status(left) == OPEN:
        if Lcounter > delay:
            print "Left Door has been open too long, closing..."
            closeDoor(L_Light)
            time.sleep(door_delay)
            print "Door should now be closed"
            Lcounter = 0
        else:
            Lcounter+=1
            print "Left Door has been open ", Lcounter, " second"
    else:
        print "Left Door is closed"
        Lcounter = 0
    time.sleep(1)
