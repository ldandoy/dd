import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug('A debug message!')


def debug(message: str, *args, **kwargs) -> None:
    logging.debug(message, *args, **kwargs)
