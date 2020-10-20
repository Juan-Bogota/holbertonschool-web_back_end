#!/usr/bin/env python3
"""Task 7 >> 7. Complex types - string and int/float to tuple"""

from typing import Callable, Union, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.
    """
    def func(n: float):
        return n * multiplier
    return func
