# coding: utf-8

from logging import getLogger, StreamHandler, DEBUG


def getCustomLogger(name):
    logger = getLogger(name)
    handler = StreamHandler()
    handler.setLevel(DEBUG)  # Change log level for purpose
    logger.setLevel(DEBUG)  # Change log level for purpose
    logger.addHandler(handler)
    logger.propagate = False
    return logger
