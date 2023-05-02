#!/usr/bin/env python3


"""Execute async_comprehension() four times in parallel using asyncio.gather
   and measure the total runtime. Return the total runtime as a float valuei
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the total runtime as a float value"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return (end - start)
