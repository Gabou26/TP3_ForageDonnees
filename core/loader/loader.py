import logging
import os

import pandas as pd


def load_file():
    """Returns a dataframe containing the data from the csv file (data.csv)
    :returns:pd.DataFrame"""
    logger = logging.getLogger("core")
    try:
        data_frame = pd.read_csv("./core/loader/data.csv", header=None)
        logger.info("Loaded data")
        _debug_dataframe(data_frame, logger)
        return data_frame
    except FileNotFoundError as err:
        print(err)

def _debug_dataframe(data_frame, logger):
    """:param df:
        :type df: pandas.DataFrame"""
    if not logger.isEnabledFor(logging.DEBUG):
        return
    for column in list(data_frame):
        logger.debug("[%s] {%s}", column, data_frame[column].unique())
