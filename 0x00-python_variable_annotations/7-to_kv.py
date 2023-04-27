#!/usr/bin/env python3
""" We combine List and Tuples from the typing module """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ We return a tuple from the given arguements """
    return (k, v**2)
