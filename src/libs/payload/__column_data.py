import logging

from typing import List
from typing import Tuple

import libs
import libs.util
import libs.util.index_with_tuple

from . import __clean_isbn as isbn

MyData = Tuple[
    # names[0] == 'Book Id'
    str,
    # names[1] = 'Title'
    str,
    # names[2] = 'Author'
    str,
    # names[5] = 'ISBN'
    str,
    # names[9] = 'Publisher'
    str,
    # names[11] = 'Number of Pages'
    str,
    # names[13] = 'Original Publication Year'
    str,
    # names[14] = 'Date Read'
    str,
    # names[15] = 'Date Added'
    str,
    # names[22] = 'Read Count'
    str
]

idxs: List[int] = [
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


def exec(items: Tuple) -> MyData:
    func = libs.util.index_with_tuple.exec
    raw_data: List = func(idxs, items)

    data: MyData = (
        str(raw_data[0]),
        str(raw_data[1]),
        str(raw_data[2]),
        isbn.exec(str(raw_data[3])),
        str(raw_data[4]),
        str(raw_data[5]),
        str(raw_data[6]),
        str(raw_data[7]),
        str(raw_data[8]),
        str(raw_data[9])
    )

    return data
