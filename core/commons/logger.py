import logging
import os

from core.commons.formatter import ColoredFormatter, formatter_message

class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(name)-20s$RESET][%(levelname)-18s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)
    def __init__(self, name):
        try:
            logging.Logger.__init__(self, "core", os.environ["DEBUG_LEVEL"].upper())
        except KeyError:
            logging.Logger.__init__(self, "core", logging.INFO) 

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return
