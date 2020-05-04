import os
import logging

from core.commons.logger import ColoredLogger
from .loader import loader
from .view import viewer
from .parser import parser

class Main:
    """Used to contain the assembly and starts the project"""

    def __init__(self):
        logging.setLoggerClass(ColoredLogger)
        self.logger = logging.getLogger("core")
        self.data_frame = ""
        self.start()

    def _debug_dataframe(self):
        """:param df:
            :type df: pandas.DataFrame"""
        if not self.logger.isEnabledFor(logging.DEBUG):
            return
        for column in list(self.data_frame):
            self.logger.debug("[%s] {%s}", column, self.data_frame[column].unique())

    def start(self):
        """Starts the application"""
        self.data_frame = loader.load_file()
        self.data_frame = parser.parse_data(self.data_frame)
        self.logger.info("Finished processing")
