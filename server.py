#!/usr/bin/env python3
"""H5 项目本地服务器 — 手机同 WiFi 扫码访问"""
import http.server
import socket
import webbrowser
import os
import sys

PORT = 8080
HOST = '0.0.0.0'

# 获取本机局域网 IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

os.chdir(os.path.dirname(os.path.abspath(__file__)))

local_ip = get_local_ip()
url = f'http://{local_ip}:{PORT}'

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({
    '.html': 'text/html; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml',
})

print(f'\n  ✅ 服务器已启动')
print(f'  📱 手机访问: {url}')
print(f'  💻 本地访问: http://localhost:{PORT}')
print(f'  ⚠️  确保手机和电脑在同一 WiFi\n')
sys.stdout.flush()

webbrowser.open(f'http://localhost:{PORT}')

with http.server.HTTPServer((HOST, PORT), handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n  👋 服务器已关闭')
        httpd.server_close()
