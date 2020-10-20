#!/usr/bin/env python3
"""Task 8 >> 8. Complex types - functions"""

from typing import Callable, Union, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.
    """
    def func(number: float):
        return number * number
    return func
