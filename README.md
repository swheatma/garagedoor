# garagedoor

This system actually consists of two separate applications.

Garage.py is a program that monitors the staus of the doors. If a door has been open for too long (as defined by the parameter ) the door will be automatically closed.

The WebIOPi program is a web based application that will display the door status, and allow a user to open an close the door from a web page.

Each application can be run separately, but the most benefit is obtained by using both applications.

USAGE
To access WebIOPi over local network
	Open a browser to http://raspberrypi:8000/ with any device of your network. Replace raspberrypi by its IP.

	Default user is "webiopi" and password is "raspberry"

The programs as supplied assume you are using the custom GaragePi PWA.  This hardware assumes the following IO

	Door-1 Sensor between pin-11 (GPIO17)
	Door-2 Sensor between pin-12 (GPIO18) 
	Door-1 output to pin-18 (GPIO24)
	Door-2 output to pin-17 (GPIO-22)
