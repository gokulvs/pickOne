from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class requestHandler(BaseHTTPRequestHandler):
	def _set_Header(self):
		self.send_response(200)
		self.send_header('Content-Type', "text/html")
		self.end_headers()

	def do_GET(self):
		self._set_Header()
		self.wfile.write("""
			<!doctype html>
				<html>
					<head>
						<title></title>
					</head>
					<body>
						<h1 style="color:blue;font-size:30px;">i will fuck you</h1>
					</body>
				</html>
				"""
		)
	def do_HEAD(self):
		self._set_Header()

def run(server_class=HTTPServer,handler_class=requestHandler,port=8080):
	server_address = ('0.0.0.0',port)
	httpd = server_class(server_address, handler_class)
	print 'starting picker v1.0'
	httpd.serve_forever()
if __name__ == "__main__":
	run()

