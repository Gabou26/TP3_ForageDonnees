import logging
import math

class Point:
    """Defines a point with 2 or more coordinates"""
    def __init__(self, *coords, nbr_coords=2):
        self.nbr_coords = nbr_coords
        self.logger = logging.getLogger("core")
        if coords and len(coords) != nbr_coords:
            self.logger.error("The number of coordinates %d is different from %d",
                              nbr_coords, len(coords))
            raise RuntimeError("The number of coordinates passed is not equal to nbr_coords")
        self.coords = coords

    def distance(self, point1, point2):
        """Calculates the euclidian distance between two points
            :param point1:
            :type point1: Point
            :param point2:
            :type point2: Point"""
        if len(self.coords) <= 0:
            self.logger.error("Coordinate not set")
            raise RuntimeError("Coordinate not set")

        if len(point1.coords) != len(point2.coords):
            self.logger.error(
                "Point 1 has %d coordinate and point 2 has %d coordinates. They must be equal", 
                len(point1.coords),
                len(point2.coords))
            raise RuntimeError("Coordinates unequal for point 1 and point 2")

        distance = 0

        for p, i in point2.coords:
            self.logger.debug("%d, %d", p, i)
            distance += math.pow((p - point1.coords[i]), 2)

        return math.sqrt(distance)
