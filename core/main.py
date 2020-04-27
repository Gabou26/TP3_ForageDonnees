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

    def start(self):
        """Starts the application"""
        self.data_frame = loader.load_file()
        self.logger.info("Finished processing")
