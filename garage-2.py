import RPi.GPIO as GPIO
import time
# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
left = 12
L_Light = 15
delay = 4
T1 = 0
T2 = 0
TE = 0
OPEN = "open"
CLOSED = "closed"
counter = 0
#check door status
def door_status(x1):
    return CLOSED if GPIO.input(x1) else OPEN

def closeDoor(door):
    GPIO.output(door, True)
    time.sleep(1)
    GPIO.output(door,False)

GPIO.output(L_Light,False)

while True:
    if door_status(left) == OPEN:
        if counter > delay:
            print "Door has been open too long, closing..."
            closeDoor(L_Light)
            counter = 0
        else:
            counter+=1
            print "Door has been open ", counter, " second"
    else:
        print "Left Door is closed"
        counter = 0
    time.sleep(1)
               
    
