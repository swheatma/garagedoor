# garagedoor
Steps to install everything


Software Installation

1. Install WebIOPi
	Download from: http://webiopi.trouch.com/DOWNLOADS.html
	Install:
		$ tar xvzf WebIOPi-x.y.z.tar.gz
		$ cd WebIOPi-x.y.z
		$ sudo ./setup.sh

2. Set static IP address on Pi:
	Edit the file /etc/dhcpcd.conf
	$ sudo nano /etc/dhcpcd.conf
	Add the following lines to the end of the file:
		interface eth0
		static ip_address=192.168.1.150 (or whatever address you want to use)

		interface wlan0
		static ip_address=192.168.1.151 (or whatever address you want to use)

		static routers=192.168.1.1 (the actual  address of your router)

3. Install Garage Door Controller:
	Copy all files to /home/pi/Projects/Garage
		This should create the html and python sub-folders
	Notes:
		The root folder will contain the config file which will need to be copied as stated below
		Python folder will contain:
			garage.py (the garage controller program)
			script.py (the web interface program)
		html foler contains index.html for the web interface


4. Copy config file to WebOIPi folder
	$sudo cp /home/pi/Projects/Garage /etc/webiopi/config

5. To start Garage program at startup:
	Make the program executable:
		$ chmod +x garage.py
	Add to startup file
		Add the following line of text to the bottom of: /home/pi/.config/lxsession/LXDE-pi/autostart
		/home/pi/Projects/Garage/python/garage.py

6. To start the web service:
	$ sudo /etc/init.d/webiopi start
   To stop the web service:
	$ sudo /etc/init.d/webiopi stop
	
   To start web service at startup:
	$ sudo update-rc.d webiopi defaults

7. Access WebIOPi over local network
	Open a browser to http://raspberrypi:8000/ with any device of your network. Replace raspberrypi by its IP.

	Default user is "webiopi" and password is "raspberry"

Hardware Installation:
1. Connect Door-1 Sensor between pin-11 (GPIO17) and Ground
2. Connect Door-2 Sensor between pin-12 (GPIO18) and Ground
3. Connect Door-1 output to pin-18 (GPIO24)
4. Connect Door-2 output to pin-17 (GPIO-22)


