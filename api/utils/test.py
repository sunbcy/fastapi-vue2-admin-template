# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 21, 2024 23:33
# ---
import socket
import urllib.request


def is_connected():
    """如果连接到公网则返回True，没有连接到则返回False。"""
    try:
        # 尝试连接到一个公共的 DNS 服务器
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(('8.8.8.8', 53))
        return True
    except OSError:
        return False


def check_proxy():
    """检查联网代理之前，先检查有没有连上公网。"""
    proxy = {}
    http_proxy = ''
    if is_connected():
        proxy_handler = urllib.request.getproxies()
        if proxy_handler:
            # print("Detected proxy settings:")
            for key, value in proxy_handler.items():
                if key == 'http':
                    # print(f"{key}: {value}")
                    http_proxy = value
                    break
            proxy['http'] = http_proxy
            proxy['https'] = http_proxy
            return proxy
        else:
            print("No proxy detected.")
            return
    else:  # 离线状态
        print("8.8.8.8:53 not connected!")
        return


print(check_proxy())
