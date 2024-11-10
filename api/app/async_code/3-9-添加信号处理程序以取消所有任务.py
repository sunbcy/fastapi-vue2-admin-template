# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: 3-9-添加信号处理程序以取消所有任务.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 10, 2024 21:20
# ---
import asyncio, signal
from asyncio import AbstractEventLoop
from typing import Set

from util.delay_functions import delay


def cancel_tasks():
    print('Got a SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Cancelling {len(tasks)} tasks')
    [task.cancel() for task in tasks]


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    await delay(10)

asyncio.run(main())
