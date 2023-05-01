#!/usr/bin/env python3
""" We span the imported function n times """
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
    and returns a list of all the delays
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    delays = []
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
