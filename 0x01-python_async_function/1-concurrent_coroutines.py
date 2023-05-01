#!/usr/bin/env python3
""" We span the imported function n times """
import random
import asyncio
from typing import List


def bubble_sort(lists: List[float]) -> List[float]:
    """ We use buuble sort to sort the list """
    n = len(lists)
    for i in range(n):
        # Flag to check if any swapping happened in this iteration
        swapped = False
        for j in range(n - i - 1):
            if lists[j] > lists[j + 1]:
                # Swap adjacent elements
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
                # Set swapped flag to true
                swapped = True
        # If no swapping happened in this iteration, the list is already sorted
        if not swapped:
            break
    return lists


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
    for task in tasks:
        delay = await task
        delays.append(delay)
    sortdelay = bubble_sort(delays)
    return sortdelay
