#!/usr/bin/env python3
""" We annote the below method """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ we return a list with tuples """
    return [(i, len(i)) for i in lst]
