"""Local server for the Niagara VFX Fast Track course.

Serves this folder on http://127.0.0.1:5178 and keeps your ticks, notes and
boss times in progress.json next to this file.

    python serve.py            (or: python serve.py 5180 for another port)
"""
import http.server
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PROGRESS = os.path.join(HERE, "progress.json")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5178


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def _json(self, code, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/progress":
            try:
                with open(PROGRESS, encoding="utf-8") as f:
                    return self._json(200, json.load(f))
            except FileNotFoundError:
                return self._json(200, {})
            except ValueError:
                return self._json(200, {})
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?")[0] != "/api/progress":
            return self._json(404, {"error": "not found"})
        n = int(self.headers.get("Content-Length", 0))
        if n > 2_000_000:
            return self._json(413, {"error": "too large"})
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return self._json(400, {"error": "bad json"})
        # write atomically so a crash never leaves a half-written file
        fd, tmp = tempfile.mkstemp(dir=HERE, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(body, f, indent=1)
        os.replace(tmp, PROGRESS)
        return self._json(200, {"ok": True})

    def log_message(self, fmt, *args):
        if "/api/" not in (args[0] if args else ""):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Niagara VFX Fast Track on http://127.0.0.1:{PORT}  (Ctrl+C to stop)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
