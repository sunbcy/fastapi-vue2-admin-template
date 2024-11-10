# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 2-24-更改slow_callback_duration.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 10, 2024 02:05
# ---
import asyncio


async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250

asyncio.run(main(), debug=True)
