from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from formatLogs import extractAddressFromRequest

a = dict(line1="|IPAdress|lastLaunched|version|lastAverageFrameRate|status|")

class serv(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/report':
            reqBody = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            ipAdress = extractAddressFromRequest(reqBody)
            a.update(line1="|IPAdress|lastLaunched|version|lastAverageFrameRate|status|")
            a.update([(ipAdress, reqBody)])
            os.system('clear')
            for val in a.values():
                print(val)
        try:
            self.send_response(200)
        except:
            self.send_response(404)

    def log_message(self, format, *args):
        return ""


httpd = HTTPServer(('0.0.0.0', 8080), serv)
httpd.serve_forever()