#!/usr/bin/env python3
""" We measure the time it takes to run a method """
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ We return the total time it takes to run a method """
    s = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e = perf_counter()
    return (e - s)
