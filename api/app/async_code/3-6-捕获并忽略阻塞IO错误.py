# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 3-6-捕获并忽略阻塞IO错误.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 10, 2024 12:27
# ---
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8001)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass
        for connection in connections:
            try:
                buffer = b''

                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        print(f'I got data: {data}!')
                        buffer = buffer + data
                print(f'All the data is: {buffer}')
                connection.send(buffer)
            except BlockingIOError:
                pass
finally:
    server_socket.close()
