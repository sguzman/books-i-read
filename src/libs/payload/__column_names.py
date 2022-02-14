import functools
import logging

from typing import List

import libs
import libs.util
import libs.util.index_with_list

from . import __column_all_names as all
from . import __column_idxs as idx


@functools.cache
def exec() -> List[str]:
    cols: List[str] = all.exec()
    idxs: List[int] = idx.exec()

    names: List[str] = []
    names = libs.util.index_with_list.exec(idxs, cols)

    return names
