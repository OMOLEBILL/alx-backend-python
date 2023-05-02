#!/usr/bin/env python3
""" The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers """
import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """ comprehensing over async_generator, then return the 10 random numbers
    """
    return [i async for i in async_generator()]
