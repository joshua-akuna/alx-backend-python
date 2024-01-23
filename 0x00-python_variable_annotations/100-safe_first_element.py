#!/usr/bin/env python3

"""
The types of the elements of the input are not known
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    the code is augmented to give the correct duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
