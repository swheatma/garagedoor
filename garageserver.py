import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.52'  # Change this to your Raspberry Pi IP address
host_port = 8080
filename = "/home/pi/Projects/garagedoor_dev/html_string2a.html"
html_string = ""
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
        global LColor, RColor

        self.do_HEAD()
        #print(html_string)
        #formattedstring = html_string.format(LDoor_color=LColor,RDoor_color=RColor)
        #print(formattedstring)
        #encodedstring = formattedstring.encode("utf-8")
        #self.wfile.write(encodedstring)
        self.wfile.write(html_string.format(LDoor_color="Yellow", RDoor_color=RColor).encode("utf-8"))

    def do_POST(self):
#       global LColor, RColor

        # check door status
        if GPIO.input(17):
            L_door_status = "Open"
            LColor = "Red"
        else:
            L_door_status = "Closed"
            LColor = "Green"
        print("Left Door: ", L_door_status, LColor)

        if GPIO.input(18):
            R_door_status = "Open"
            RColor = "Red"
        else:
            R_door_status = "Closed"
            RColor = "Green"
        print("Right Door: ", R_door_status, RColor)


        # check for button press
        content_length = int(self.headers['Content-Length'])
        #print(content_length)
        body = self.rfile.read(content_length)
        #print("body =", body)
        body2 = body.decode('utf-8')
        #print("Body2 = ", body2)
        body3 = body2.split("door=",1)[1]
        #print(body3)

        if body3 == "Door-1":
           print("You pressed Left-Door")
           GPIO.output(22, GPIO.HIGH)
           sleep(1.25)
           GPIO.output(22, GPIO.LOW)
        elif body3 == "Door-2":
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
