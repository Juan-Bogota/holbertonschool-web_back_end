#!/usr/bin/env python3
"""Task 10 >> 10. Duck typing - first element of a sequence"""

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function safe first element"""
    if lst:
        return lst[0]
    else:
        return None
