from core.algorithm.knn.knn import Knn
from core.commons.point import Point

def run(data_frame):
    """Runs the algorithms"""
    points = []

    for i, row in data_frame.iterrows():
        points.append(
            Point(
                row[0],
                row[2],
                row[3],
                row[4],
                row[5],
                row[9],
                row[10],
                row[11],
                row[12],
                nbr_coords=9))

    knn = Knn(points)
    knn.debug()
    