#!/usr/bin/env python3


"""Execute async_comprehension() four times in parallel using asyncio.gather
   and measure the total runtime. Return the total runtime as a float value.
"""


import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Return the total runtime as a float value """
    start = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = perf_counter()
    return (end - start)
