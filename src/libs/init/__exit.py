import atexit
import logging


def exec() -> None:
    atexit.register(lambda: logging.debug('bye'))
