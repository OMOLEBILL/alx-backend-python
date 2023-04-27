#!/usr/bin/env python3
""" We try to impliment Type Notation """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ We return a zoomed in tuple """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
