# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 2-19-任务的CPU密集型代码.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 09, 2024 13:38
# ---
import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))
    await task_one
    await task_two
    await delay_task

asyncio.run(main())
