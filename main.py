import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
PORT = int(os.environ.get("PORT") or os.environ.get("APP_PORT") or 8000)
VERSION, BRANCH = "v1", "python"
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health"):
            b = json.dumps({"status":"ok","runtime":"python","source":"github","version":VERSION,"branch":BRANCH}, separators=(",",":")).encode()
            self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
        else:
            self.send_response(404); self.end_headers()
    def log_message(self,*a): pass
if __name__ == "__main__":
    print(f"gh python {VERSION} branch={BRANCH} on {PORT}")
    HTTPServer(("0.0.0.0", PORT), H).serve_forever()
