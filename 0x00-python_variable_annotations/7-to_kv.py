#!/usr/bin/env python3
"""Defines the to_kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    the typed annotated funtion takes a string k and an int or
    float v as arguments and returns a Tuple with the value of
    k as  the first element and the square of v as float as the
    second element.
    """
    return (k, (v * v))
