# Steps to install everything #

## Setup Raspberry Pi ##
1. Install Raspian
	Download latest Raspian to your PC
2. To enable SSH: create an empty file in the root os the SD card called "ssh" (no extension)
3. To enable WiFi create a file called wpa_supplicant.conf
	Enter the following data:
```
country=us
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
scan_ssid=1
ssid="MyNetworkSSID" #enter your network SSID
psk="Pa55w0rd1234"  #enter your Wifi password
}
```
4. Insert SD card into Raspberry Pi and boot up
5. Connect to Raspberry Pi using ssh (ssh raspberrypi)
	username = pi
	password = raspberry

	Use ifconfig to find the ip addres of your raspberry pi

6. Update the raspian OS
```
$sudo apt-get update
$sudo apt-get upgrade
```
7. If you want to connect to raspberry pi using vnc, enable it in the configuration
```
$sudo raspi-config
```
8. Set static IP address on Pi:
	Edit the file /etc/dhcpcd.conf
```
$ sudo nano /etc/dhcpcd.conf
```
  Add the following lines to the end of the file:
```
interface eth0
static ip_address=192.168.1.150 (or whatever address you want to use)

interface wlan0
static ip_address=192.168.1.151 (or whatever address you want to use)

static routers=192.168.1.1 (the actual  address of your router)
```
9. Reboot the raspberry pi to make the changes take effect
```
$sudo reboot
```

## Garage Door Application Software Installation ##

1. Install WebIOPi
```
wget http://sourceforge.net/projects/webiopi/files/webiopi-0.7.1.tar.gz
```
Or download from: http://webiopi.trouch.com/DOWNLOADS.html
	Install:

```  
$ tar xvzf WebIOPi-x.y.z.tar.gz
$ cd WebIOPi-x.y.z
$ sudo ./setup.sh
```
2. Install Garage Door Controller:
	    Go to the folder: /home/pi/Projects
```
$ cd /home/pi/Projects
```
Copy the files from GitHub:
```
$ git clone https://github.com/swheatma/garagedoor
```

This will create a folder called garagedoor in the current folder.
- Notes:
  - This should create the html and python sub-folders. 
    - The root folder will contain the config file which will need to be copied as stated below 
    - The python folder will contain: 
      - garage.py (the garage controller program) 
      - script.py (the web interface program) 
    - The html folder contains index.html for the web interface
	
3. Make the program executable:
```
$ chmod +x /home/pi/Projects/garagedoor/python/garage.py
```
4. Copy config file to WebOIPi folder
```
$sudo cp /home/pi/Projects/Garage /etc/webiopi/config
```
You may need to edit the config file so that the GPIO settings match your hardware.
	
5. To start the web service:
```
$ sudo /etc/init.d/webiopi start
```
To stop the web service:
```
$ sudo /etc/init.d/webiopi stop
```	
6. To start Garage program at startup: 

	Option-1: 
	
  Add to LXDE-pi/autostart file 
	Add the following line of text to the bottom of: /home/pi/.config/lxsession/LXDE-pi/autostart 
	/home/pi/Projects/garagedoor/python/garage.py 
	
Option-2: 
	Add to crontab 
	
  Edit the crontab file 
```
$ sudo crontab -e 
```
add the following line: 
```
@reboot python /home/pi/Projects/garagedoor/python/garage.py & 
```
to add a delay before the program starts (recommended) 
```
@reboot sleep 20 && python /home/pi/Projects/garagedoor/python/garage.py &
```

   To start web service at startup:
```   
$ sudo update-rc.d webiopi defaults
```

7. Access WebIOPi over local network
	Open a browser to http://raspberrypi:8000/ with any device of your network. Replace raspberrypi by its IP.

	Default user is "webiopi" and password is "raspberry"

## Hardware Installation: ##

1. Connect Door-1 Sensor between pin-11 (GPIO17) and Ground
2. Connect Door-2 Sensor between pin-12 (GPIO18) and Ground
3. Connect Door-1 output to pin-18 (GPIO24)
4. Connect Door-2 output to pin-17 (GPIO-22)
