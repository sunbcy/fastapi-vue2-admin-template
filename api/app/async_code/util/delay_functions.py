# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: delay_functions.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 08, 2024 21:50
# ---
import asyncio


async def delay(delay_seconds:int) -> int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} seconds')
    return delay_seconds
