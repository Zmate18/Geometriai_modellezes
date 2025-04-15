import numpy as np

def de_casteljau(points, t):
    points = np.array(points)
    n = len(points)
    for r in range(1, n):
        points = (1 - t) * points[:-1] + t * points[1:]
    return points[0]

def bezier_curve(control_points, steps=100):
    return [de_casteljau(control_points, t) for t in np.linspace(0, 1, steps)]