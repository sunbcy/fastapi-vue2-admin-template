# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 2-20-在协程中错误地使用阻塞API.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 09, 2024 13:44
# ---

import asyncio
import requests
from util import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get(f'http://www.baidu.com').status_code


@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3

asyncio.run(main())
