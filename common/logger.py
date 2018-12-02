# coding: utf-8

from logging import getLogger, StreamHandler, DEBUG


def get_custom_logger(name):
    """ return a logger object.
    :param name: Function name
    :return: logger object
    """
    logger = getLogger(name)
    handler = StreamHandler()
    handler.setLevel(DEBUG)  # Change log level according to purpose
    logger.setLevel(DEBUG)  # Change log level according to purpose
    logger.addHandler(handler)
    logger.propagate = False
    return logger
