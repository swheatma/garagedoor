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
	Go to the folder: /home/pi/Projects
		$ cd /home/pi/Projects
	Copy the files from GitHub:
		$ git clone https://github.com/swheatma/garagedoor
	This will create a folder called garagedoor in the current folder.
	Notes:
		This should create the html and python sub-folders
		The root folder will contain the config file which will need to be copied as stated below
		The python folder will contain:
			garage.py (the garage controller program)
			script.py (the web interface program)
		The html folder contains index.html for the web interface

4. Copy config file to WebOIPi folder
	$sudo cp /home/pi/Projects/garagedoor/config-garage /etc/webiopi/config

5. To start Garage program at startup:
	Make the program executable:
		$ chmod +x garage.py
	Option-1:
		Add to LXDE-pi/autostart file
		Add the following line of text to the bottom of: /home/pi/.config/lxsession/LXDE-pi/autostart
		/home/pi/Projects/garagedoor/python/garage.py
	Option-2:
		Add to crontab
		Edit the crontab file
		$ sudo crontab -e
		add the following line:
		@reboot python /home/pi/Projects/garagedoor/python/garage.py &
		to add a delay before the program starts (recommended)
		@reboot sleep 20 && python /home/pi/Projects/garagedoor/python/garage.py &

6. To start web service at startup:
	$ sudo update-rc.d webiopi defaults

7. Access WebIOPi over local network
	Open a browser to http://raspberrypi:8000/ with any device of your network. Replace raspberrypi by its IP.

	Default user is "webiopi" and password is "raspberry"

Hardware Installation:
1. Connect Door-1 Sensor between pin-11 (GPIO17) and Ground
2. Connect Door-2 Sensor between pin-12 (GPIO18) and Ground
3. Connect Door-1 output to pin-18 (GPIO24)
4. Connect Door-2 output to pin-17 (GPIO-22)


