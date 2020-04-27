import logging
import pandas

from core.mappers.scholarship_map import string_to_tag as scholarship
from core.mappers.jobs_map import string_to_tag as jobs

def parse_data(data_frame):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    logger = logging.getLogger("core")
    logger.info("Parsing data")

    return  _map_data(data_frame, logger)

def _map_data(data_frame, logger):
    """
        :param data_frame:
        :type data_frame: pandas.DataFrame
        :param logger:
        :type logger: logging.Logger
    """
    logger.debug("Mapping dataframe scholarship string to number")
    data_frame[3] = data_frame[3].map(scholarship)
    logger.debug("Done mapping scholarship string to number")

    logger.debug("Mapping dataframe job string to number")
    data_frame[1] = data_frame[1].map(jobs)
    logger.debug("done mapping job string to number")
    
    return data_frame