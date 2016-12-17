import webiopi
#SW import datetime

GPIO = webiopi.GPIO

LIGHT = 22 # GPIO pin using BCM numbering
LIGHT2 = 24

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)
    GPIO.setFunction(LIGHT2, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
#SW    now = datetime.datetime.now()

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
    GPIO.digitalWrite(LIGHT2, GPIO.LOW)
