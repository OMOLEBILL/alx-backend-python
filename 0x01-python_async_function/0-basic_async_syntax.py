#!/usr/bin/env python3
""" This Scripts shows the bbasic usage of random.uniform """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ This script return a  random number """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
