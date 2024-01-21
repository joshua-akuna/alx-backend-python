#!/usr/bin/env python3
"""Defines the make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as an argument"""
    def base_multiplier(m: float) -> float:
        """returns a function that multiplies a float by a multiplier"""
        return (multiplier * m)
    return base_multiplier
