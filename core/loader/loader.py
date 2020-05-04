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
        return data_frame
    except FileNotFoundError as err:
        logger.error(err)
