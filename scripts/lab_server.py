#!/usr/bin/env python3
"""Serve the CI candidate with the text compression used by GitHub Pages."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from pathlib import Path
import gzip


class CompressedFiles(SimpleHTTPRequestHandler):
    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            if not self.path.split('?', 1)[0].endswith('/'):
                return super().send_head()
            path /= 'index.html'
        mime = self.guess_type(str(path))
        compressible = mime.startswith('text/') or mime in {
            'application/javascript', 'application/json', 'application/xml', 'image/svg+xml'}
        if path.is_file() and compressible and 'gzip' in self.headers.get('Accept-Encoding', ''):
            payload = gzip.compress(path.read_bytes(), compresslevel=6, mtime=0)
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.send_header('Content-Encoding', 'gzip')
            self.send_header('Vary', 'Accept-Encoding')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            return BytesIO(payload)
        return super().send_head()


if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 4175), partial(CompressedFiles, directory='_site'))
    server.serve_forever()
