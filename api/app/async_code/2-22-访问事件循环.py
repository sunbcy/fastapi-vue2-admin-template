# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 2-22-访问事件循环.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 10, 2024 01:34
# ---
import asyncio
from util import delay


def call_later():
    print("I'm bing called in the future!")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main())
