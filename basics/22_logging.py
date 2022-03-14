# Different loggings.
# debug: logging.debug("debug message").
# info: logging.info("info message").
# warning: logging.warning("warning message").
# error: logging.error("error message").
# critical: logging.critical("critical message").
# json logger: https://github.com/madzak/python-json-logger

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.debug("It's a debug message.")
logging.info("It's a info message.")
logging.warning("it's a warning message.")
logging.error("It's a error message.")
logging.critical("It's a critical message.")