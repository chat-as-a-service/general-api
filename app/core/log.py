import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"


def getLogger(name):
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    return logging.getLogger(name)
