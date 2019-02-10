# coding: utf-8

import common.logger as custom_logger
from webapp import *
import json


logger = custom_logger.get_custom_logger(__name__)


def main():
    config_json = open("config.json", 'r')
    config = json.load(config_json)
    host = config["host"]
    port = config["port"]
    debug = config["debug"]
    mongo_host = config["mongo"]["host"]
    mongo_port = config["mongo"]["port"]
    app = WebApp(host=host, port=port, debug=debug, mongo_host=mongo_host, mongo_port=mongo_port)
    app.start()


if __name__ == '__main__':
    logger.info("Start expression-viewer")
    main()

