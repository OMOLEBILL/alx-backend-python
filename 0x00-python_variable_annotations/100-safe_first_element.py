#!/usr/bin/env python3
""" We impliment Duck-typing """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ We return a value or None """
    if lst:
        return lst[0]
    else:
        return None
