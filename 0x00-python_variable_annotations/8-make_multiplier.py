#!/usr/bin/env python3
""" we return a callable from the Typing module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a func that multiplies a float by float """
    def mutlipy(x: float) -> float:
        """ The function that we return """
        return x * multiplier
    return mutlipy
