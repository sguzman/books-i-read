from typing import List
from typing import Tuple


def exec(idxs: List[int], data: Tuple) -> List:
    index_data: List = []

    for idx in idxs:
        index_data.append(data[idx])

    return index_data
