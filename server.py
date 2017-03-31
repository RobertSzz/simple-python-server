from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi

PORT_NUMBER = 8080

#class for request handling
class myHandler(BaseHTTPRequestHandler):

	#handler for GET request
	def do_GET(self):
		if self.path=="/":
			self.path="/response.html"

		try:
			f = open(curdir + sep + self.path) 
			self.send_response(200) #add status code
			self.send_header('Content-type', 'text/html') #proper mimetype
			self.end_headers() #close headers
			self.wfile.write(f.read()) #add file to response
			f.close()

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

#starting server script			
try:
	#create server instance
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started server on port ' , PORT_NUMBER

	#run server
	server.serve_forever()

except KeyboardInterrupt:
	print 'KeyboardInterrupt received, shutting server down'
	server.socket.close()