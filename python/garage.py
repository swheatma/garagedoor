#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# set variables
left = 11    #GPIO17
right = 12   #GPIO18
R_Light = 15 #GPIO22
L_Light = 16 #GPIO23
delay = 180     #door open limit in seconds

OPEN = "open"
CLOSED = "closed"
RClosed = time.time()
RElapsed = 0
LElapsed = 0

door_delay = 15  # Time is takes for the door to close (in seconds)

# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) # use GPIO pinout references (not GPIO number)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)
GPIO.setup(R_Light, GPIO.OUT)
GPIO.setup(L_Light, GPIO.OUT)


#check door status
def door_status(x1):
    return OPEN if GPIO.input(x1) else CLOSED

def closeDoor(door):
    GPIO.output(door, False)
    time.sleep(1)
    GPIO.output(door,True)

GPIO.output(R_Light,True)
GPIO.output(L_Light,True)

while True:
    if door_status(right) == OPEN:
        RElapsed = time.time() - RClosed
        if RElapsed > delay:
            print "Right Door has been open ", RElapsed, " second"
            print "Right Door has been open too long, closing..."
            closeDoor(R_Light)
            time.sleep(door_delay)
            print "Door should now be closed"
        else:
            RElapsed = time.time() - RClosed
            print "Right Door has been open ", RElapsed, " second"
    else:
        print "Right Door is closed"
        RClosed = time.time()
    if door_status(left) == OPEN:
        LElapsed = time.time() - LClosed
        if LElapsed > delay:
            print "Left Door has been open ", LElapsed, " second"
            print "Left Door has been open too long, closing..."
            closeDoor(L_Light)
            time.sleep(door_delay)
            print "Door should now be closed"
        else:
            LElapsed = time.time() - LClosed
            print "Left Door has been open ", LElapsed, " second"
    else:
        print "Left Door is closed"
        LClosed = time.time()
    time.sleep(1)
