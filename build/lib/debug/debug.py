import logging


class debug:

    def debug(msg):
        logging.basicConfig(level=logging.DEBUG)
        return logging.debug(msg)
