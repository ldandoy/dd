import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug('Logger have successfully started')


def debug(message: str, *args, **kwargs) -> None:
    logging.debug(f' {message}', *args, **kwargs)
