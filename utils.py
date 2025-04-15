def bezier_length(curve_points):
    length = 0
    for i in range(len(curve_points) - 1):
        x0, y0 = curve_points[i]
        x1, y1 = curve_points[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        length += (dx ** 2 + dy ** 2) ** 0.5
    return length