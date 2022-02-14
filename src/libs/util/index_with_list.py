from typing import List


def exec(idxs: List[int], data: List) -> List:
    index_data: List = []

    for idx in idxs:
        index_data.append(data[idx])

    return index_data
