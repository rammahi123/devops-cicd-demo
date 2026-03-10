from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"Hello from Kubernetes DevOps Demo!")

PORT = 80
server = HTTPServer(("", PORT), handler)
print("Server running on port 80...")
server.serve_forever()
