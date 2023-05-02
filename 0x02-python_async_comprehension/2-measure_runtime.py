#!/usr/bin/env python3
"""Execute async_comprehension() four times in parallel using asyncio.gather
   and measure the total runtime. Return the total runtime as a float value.
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Return the total runtime as a float value """
    start = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = asyncio.get_running_loop().time()
    return end - start
