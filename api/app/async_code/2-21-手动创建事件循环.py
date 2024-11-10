# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 2-21-手动创建事件循环.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 10, 2024 01:32
# ---
import asyncio


async def main():
    await asyncio.sleep(1)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
