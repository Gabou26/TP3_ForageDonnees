import logging

class Knn:
    """Implements the KNN algorithm"""
    def __init__(self, points):
        self.logger = logging.getLogger("core")
        self.points = points

    def debug(self):
        """Just debugging"""
        self.logger.debug("Number of points: %d", len(self.points))

