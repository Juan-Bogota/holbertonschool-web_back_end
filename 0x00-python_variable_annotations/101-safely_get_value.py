#!/usr/bin/env python3
"""Task 11 >> 11. More involved type annotations """

from typing import Mapping, Union, Sequence, Any, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'), None]
                     = None) -> Union[Any, TypeVar('T')]:
                     """Function safely_get_value"""

    if key in dct:
        return dct[key]
    else:
        return default
