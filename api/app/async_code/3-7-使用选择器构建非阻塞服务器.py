# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 3-7-使用选择器构建非阻塞服务器.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 10, 2024 12:36
# ---
import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8001)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print('No events, waiting a bit more!')
    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {address}')
            selector.register(connection, selector.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f'I got some data: {data}')
            event_socket.send(data)
