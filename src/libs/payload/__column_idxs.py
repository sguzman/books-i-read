import functools
import logging

from typing import List


@functools.cache
def exec() -> List[int]:
    return [
        0,
        1,
        2,
        5,
        9,
        11,
        13,
        14,
        15,
        22
    ]
