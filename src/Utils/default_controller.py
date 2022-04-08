import logging
from datetime import datetime


class DefaultController:

    def __init__(self):
        now = datetime.now()
        logging.basicConfig(filename='logs/' + now.strftime("%m%d%Y") + '.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.warning("This is a debug message")
