#!/usr/bin/env python3
"""Defines the safely_get_value function"""

import typing
from typing import Mapping, Any, Union


T = typing.TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
