from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PARTICIPANT_NAME = os.getenv("PARTICIPANT_NAME","Participant")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Hello {PARTICIPANT_NAME} from EKS Application".encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Server running on port 8080")
server.serve_forever()