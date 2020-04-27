import sys
import logging

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def update_view(data_frame):
    """Plots the graphs with the data provided"""
    logger = logging.getLogger("core")
    logger.info("Updating view")


def _maximize(manager, plotter):
    if sys.platform.startswith("linux") and plotter.get_backend() == "TkAgg":
        manager.resize(*manager.window.maxsize())
    elif plotter.get_backend() == "TkAgg":
        manager.window.state('zoomed')
    elif plotter.get_backend() == "wxAgg":
        manager.frame.Maximize(True)
    elif plotter.get_backend() == "Qt4Agg":
        manager.window.showMaximized()
