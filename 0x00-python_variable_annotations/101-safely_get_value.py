#!/usr/bin/env python3
"""Defines the safely_get_value function"""

from typing import Mapping, Any, Union
import typing


T = typing.TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Given the parameters and return values, add type annotations
    to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
