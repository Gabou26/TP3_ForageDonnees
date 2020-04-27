import logging
import pandas

from core.mappers.scholarship_map import *

def parse_data(data_frame):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    logger = logging.getLogger("core")
    logger.info("Parsing data")

    parsed_data_frame = _map_data(data_frame)

def _map_data(data_frame):
    """
        :param data_frame:
        :type data_frame: pandas.DataFrame
    """
    
    return data_frame