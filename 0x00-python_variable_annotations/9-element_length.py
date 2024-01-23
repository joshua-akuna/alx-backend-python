#!/usr/bin/env python3

"""The module defines the element_length function"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a collection of tuples"""
    return [(i, len(i)) for i in lst]
