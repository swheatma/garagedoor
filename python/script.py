import webiopi

GPIO = webiopi.GPIO

DOOR1 = 22 # GPIO pin using BCM numbering
DOOR2 = 23
DOOR3 = 24

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(DOOR1, GPIO.OUT)
    GPIO.setFunction(DOOR2, GPIO.OUT)
    GPIO.setFunction(DOOR3, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(DOOR1, GPIO.LOW)
    GPIO.digitalWrite(DOOR2, GPIO.LOW)
    GPIO.digitalWrite(DOOR3, GPIO.LOW)