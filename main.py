import http.server
import socketserver
import random
from yollor import *
import os

tagn1 = f"{c.black('[')}{c.purple('1')}{c.black(']')}"
tagn2 = f"{c.black('[')}{c.purple('2')}{c.black(']')}"
hashtag = f"{c.black('[')}{c.purple('#')}{c.black(']')}"

ban1 = rf"""
                                                                                   
      _/_/                _/      _/      _/_/_/    _/_/_/                _/_/_/   
   _/    _/  _/_/_/    _/_/_/_/          _/    _/  _/    _/    _/_/    _/          
  _/_/_/_/  _/    _/    _/      _/      _/    _/  _/    _/  _/    _/    _/_/       
 _/    _/  _/    _/    _/      _/      _/    _/  _/    _/  _/    _/        _/      
_/    _/  _/    _/      _/_/  _/      _/_/_/    _/_/_/      _/_/    _/_/_/         
                                                                                   
Anti DDoS & Server Host Tool"""
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{c.black(ban1)}")

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        user_ip = self.client_address[0]
        if user_ip in request_count and request_count[user_ip] >= request_limit:
            request_line = f"{c.red('Seu servidor está sofrendo um ataque DoS/DDoS, iniciando medidas protetivas')}"
        else:
            request_line = f"{c.purple('<--')} {c.purple('|')} {c.black(format % args)} {c.purple('|')} {c.cyan(self.headers.get('User-Agent', 'Unknown').split('(')[0].strip())} {c.purple('|')} {c.purple(user_ip)} {c.purple('|')} {c.purple('-->')}"
            request_count[user_ip] = request_count.get(user_ip, 0) + 1
        print(request_line)

port = 5500

handler = CustomHTTPRequestHandler
request_count = {}
request_limit = 8

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Servidor rodando em http://localhost:{port}")
    httpd.serve_forever()
