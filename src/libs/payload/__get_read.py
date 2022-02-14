import logging
from typing import List

from . import __column_data as cold


def exec(list: List[cold.MyData]) -> List[cold.MyData]:
    sub_list: List[cold.MyData] = []

    for row in list:
        read_count: int = int(row[-1])
        title: str = row[1]

        if read_count > 0:
            logging.debug('Read book %s %d times', title, read_count)
            sub_list.append(row)

    return sub_list
