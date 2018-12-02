# coding: utf-8

import common.logger as custom_logger
from webapp import *


logger = custom_logger.get_custom_logger(__name__)


def main():
    host = '0.0.0.0'
    port = 8080
    debug = True
    app = WebApp(host=host, port=port, debug=debug)
    app.start()


if __name__ == '__main__':
    logger.info("Start expression-viewer")
    main()

