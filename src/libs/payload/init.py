import logging

from typing import List
from typing import Tuple

from . import __column_choice as choice
from . import __column_data as cold
from . import __column_names as names
from . import __data as data
from . import __get_read as read
from . import __sort_key as sort_key


def exec() -> None:
    dump: List[Tuple] = data.exec()
    title: List[str] = names.exec()
    logging.debug("Got data, size='%s'", len(str(dump)))

    cleaned: List[cold.MyData] = choice.exec(dump)
    logging.debug("Column titles: %s", str(title))
    print(*title, sep=",")

    rd: List[cold.MyData] = read.exec(cleaned)
    logging.debug("Read %d books", len(rd))

    func = sort_key.exec
    rd.sort(key=func, reverse=True)

    logging.debug("Sorted order of books")
    for idx, book in enumerate(rd):
        logging.debug("[%d] %s", idx, book)
        print(idx, *book, sep=",")
