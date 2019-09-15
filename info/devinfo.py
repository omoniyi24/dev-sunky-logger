import logging


class DevInfo:

    def dev_info(self, msg):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        return logging.info(msg)
