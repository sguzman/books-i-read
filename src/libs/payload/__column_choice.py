import logging

from typing import List
from typing import Tuple

import libs
import libs.util
import libs.util.index_with_list

from . import __column_data as cold


def exec(data: List[Tuple]) -> List[cold.MyData]:
    # names[0] == 'Book Id'
    # names[1] = 'Title'
    # names[2] = 'Author'
    # names[3] = 'Author l-f'
    # names[4] = 'Additional Authors'
    # names[5] = 'ISBN'
    # names[6] = 'ISBN13'
    # names[7] = 'My Rating'
    # names[8] = 'Average Rating'
    # names[9] = 'Publisher'
    # names[10] = 'Binding'
    # names[11] = 'Number of Pages'
    # names[12] = 'Year Published'
    # names[13] = 'Original Publication Year'
    # names[14] = 'Date Read'
    # names[15] = 'Date Added'
    # names[16] = 'Bookshelves'
    # names[17] = 'Bookshelves with positions'
    # names[18] = 'Exclusive Shelf'
    # names[19] = 'My Review'
    # names[20] = 'Spoiler'
    # names[21] = 'Private Notes'
    # names[22] = 'Read Count'
    # names[23] = 'Recommended For'
    # names[24] = 'Recommended By'
    # names[25] = 'Owned Copies'
    # names[26] = 'Original Purchase Date'
    # names[27] = 'Original Purchase Location'
    # names[28] = 'Condition'
    # names[29] = 'Condition Description'
    # names[30] = 'BCID'

    names: List[cold.MyData] = []
    for idx, items in enumerate(data):
        d: cold.MyData = cold.exec(items)
        logging.debug('[%d] %s', idx, str(d))

        names.append(d)

    return names
