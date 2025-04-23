def bezier_length(curve_points):
    length = 0
    for i in range(len(curve_points) - 1):
        x0, y0 = curve_points[i]
        x1, y1 = curve_points[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        length += (dx ** 2 + dy ** 2) ** 0.5
    return length

def estimate_area(points: list[tuple[int, int]]) -> float:
    if len(points) < 3:
        return 0.0

    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)

    return abs(area) / 2