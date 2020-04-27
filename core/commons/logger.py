import logging
import os

from core.commons.formatter import ColoredFormatter, formatter_message

class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(name)-6s$RESET][%(levelname)-18s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)

    def __init__(self, name):
        logging.addLevelName(9, "TRACE")
        logging.Logger.trace = self.trace

        try:
            logging.Logger.__init__(self, "core", os.environ["DEBUG_LEVEL"].upper())
        except KeyError:
            logging.Logger.__init__(self, "core", logging.INFO)

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)
        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return

    def trace(self, message, *args, **kws):
        """"""
        if self.isEnabledFor(9):
        # Yes, logger takes its '*args' as 'args'.
            self._log(9, message, args, **kws)
