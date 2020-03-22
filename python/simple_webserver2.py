import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.52'  # Change this to your Raspberry Pi IP address
host_port = 8000
pin17 = 0


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global pin17
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html>
           <head>
           <title>Garage Door</title>
           </head>
           <body style="width:960px; margin: 20px auto;">
           <h1>Welcome to my Raspberry Pi</h1>
           <p>Door Status: {}</p>
           <form action="/">
               <button formmethod="post" type="submit">Toggle Door</button>
           </form>
           </body>
           </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        door_status = 'The door is currently '
        if GPIO.input(17) or pin17 == 1:
            door_status+= "open."
        else:
            door_status+= "closed."
                
        self.wfile.write(html.format(door_status).encode("utf-8"))
        
    def do_POST(self):
        global pin17
        GPIO.output(22, GPIO.HIGH)
        sleep(1.25)
        GPIO.output(22, GPIO.LOW)
        pin17=(pin17+1)%2
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
        GPIO.setup(22, GPIO.OUT)

if __name__ == '__main__':
    init()
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
