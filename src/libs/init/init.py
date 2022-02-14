import functools
from typing import List
from typing import Tuple

from . import __log as log
from . import __exit as exit
from . import __greet as greet


@functools.cache
def exec() -> None:
    log.exec()
    greet.exec()
    exit.exec()
