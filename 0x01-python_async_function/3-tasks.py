#!/usr/bin/env python3
""" We return an asyncio task """
import asyncio 
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ We return an asycio.Task """
    return asyncio.create_task(wait_random(max_delay))
