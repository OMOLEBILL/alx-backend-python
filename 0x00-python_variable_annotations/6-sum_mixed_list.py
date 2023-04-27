#!/usr/bin/env python3
""" we mix types and use the union module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """We return the sum of the mixed types"""
    return sum(mxd_lst)
