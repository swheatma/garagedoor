import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.52'  # Change this to your Raspberry Pi IP address
host_port = 8080
filename = "/home/pi/Projects/garagedoor_dev/html_string2a.html"
pin17 = 0
html_string = ""
door1 = 0
door2 = 0
LColor = "Yellow"
RColor = "Yellow"

with open(filename)  as f:
    html_string = f.read()

class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global pin17, LColor, RColor

        self.do_HEAD()
        L_door_status = 'The left door is currently '
        if GPIO.input(17):
            L_door_status = "Open"
            LColor = "Green"
        else:
            L_door_status = "Closed"
            LColor = "Red"
        print("Left Door: ", L_door_status)

        R_door_status = 'The right door is currently '
        if GPIO.input(18):
            R_door_status = "Open"
            RColor = "Green"
        else:
            R_door_status = "Closed"
            RColor = "Red"
        print("Right Door: ", R_door_status)

        #print(html_string)
        formattedstring = html_string.format(LColor,RColor_status)
        #print(formattedstring)
        encodedstring = formattedstring.encode("utf-8")
        self.wfile.write(encodedstring)

    def do_POST(self):
#        global pin17

        content_length = int(self.headers['Content-Length'])
        print(content_length)
        body = self.rfile.read(content_length)
        print("body =", body)
        body2 = body.decode('utf-8')
        print("Body2 = ", body2)
        body3 = body2.split("door=",1)[1]
        print(body3)

        if body3 == "LDoor":
           print("You pressed Left-Door")
           GPIO.output(22, GPIO.HIGH)
           sleep(1.25)
           GPIO.output(22, GPIO.LOW)
        elif body3 == "RDoor":
           print("You pressed Right-Door")
           GPIO.output(23, GPIO.HIGH)
           sleep(1.25)
           GPIO.output(23, GPIO.LOW)

       	self._redirect('/')

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()
        
def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17, GPIO.IN)
        GPIO.setup(18, GPIO.IN)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

if __name__ == '__main__':
    init()
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
