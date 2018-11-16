"""
Plot a square on H2 with Poincare Disk visualization.
"""

import matplotlib.pyplot as plt
import numpy as np

import geomstats.visualization as visualization

from geomstats.hyperbolic_space import HyperbolicSpace

H2 = HyperbolicSpace(dimension=2)
METRIC = H2.metric

SQUARE_SIZE = 50


def main():
    top = SQUARE_SIZE / 2.0
    bot = - SQUARE_SIZE / 2.0
    left = - SQUARE_SIZE / 2.0
    right = SQUARE_SIZE / 2.0
    corners_int = [(bot, left), (bot, right), (top, right), (top, left)]
    corners_ext = H2.intrinsic_to_extrinsic_coords(corners_int)
    n_steps = 20
    for i, src in enumerate(corners_ext):
        dst_id = (i+1) % len(corners_ext)
        dst = corners_ext[dst_id]
        tangent_vec = METRIC.log(point=dst, base_point=src)
        geodesic = METRIC.geodesic(initial_point=src,
                                   initial_tangent_vec=tangent_vec)
        t = np.linspace(0, 1, n_steps)
        edge_points = geodesic(t)

        ax = plt.gca()
        visualization.plot(
            edge_points,
            ax=ax,
            space='H2_poincare_half_plane',
            marker='.',
            color='black')

    plt.show()


if __name__ == "__main__":
    main()
