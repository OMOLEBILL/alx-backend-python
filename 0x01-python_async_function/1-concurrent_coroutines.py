#!/usr/bin/env python3
""" We span the imported function n times """
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
    and returns a list of all the delays
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
