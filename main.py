# coding: utf-8

import common.logger as custom_logger
from webapp import *


logger = custom_logger.get_custom_logger(__name__)


def main():
    app = WebApp()


if __name__ == '__main__':
    logger.info("Start expression-viewer")
    main()

