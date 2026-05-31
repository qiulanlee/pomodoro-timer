#!/usr/bin/env python3
"""番茄钟启动器 —— 启动本地服务并在浏览器中打开"""

import http.server
import os
import sys
import webbrowser
import socket
import signal

DIR = os.path.dirname(os.path.abspath(__file__))


def find_free_port(start=8765):
    """找一个空闲端口"""
    for port in range(start, start + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        # 静默日志
        pass


def main():
    port = find_free_port()
    url = f'http://127.0.0.1:{port}'

    server = http.server.HTTPServer(('127.0.0.1', port), Handler)

    print(f'🍅 番茄钟已启动 → {url}')
    print('在浏览器中操作，关闭此窗口即可退出。')
    print()

    # 打开浏览器
    webbrowser.open(url)

    # 处理 Ctrl+C 优雅退出
    signal.signal(signal.SIGINT, lambda *_: (print('\n👋 番茄钟已退出'), server.shutdown(), sys.exit(0)))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n👋 番茄钟已退出')


if __name__ == '__main__':
    main()
