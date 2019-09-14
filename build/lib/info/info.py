import logging


class info:

    def info(msg):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        return logging.info(msg)
