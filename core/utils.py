def bezier_length(curve_points):
    """
    Kiszámítja a Bézier görbe hosszát a pontok közötti euklideszi távolságok összeadásával.

    Paraméterek:
        curve_points (list of tuple): A görbén elhelyezkedő pontok listája.

    Visszatérési érték:
        float: A görbe teljes hossza pixelben.
    """
    length = 0
    for i in range(len(curve_points) - 1):
        x0, y0 = curve_points[i]
        x1, y1 = curve_points[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        length += (dx ** 2 + dy ** 2) ** 0.5
    return length

def estimate_area(points: list[tuple[int, int]]) -> float:
    """
    A megadott pontok által körbezárt terület becslése a saru-formula alapján.

    Paraméterek:
        points (list of tuple): A csúcspontok, amiket a görbe alkot.

    Visszatérési érték:
        float: A terület nagysága négyzetpixelben. Ha kevesebb mint 3 pont van, akkor 0.
    """
    if len(points) < 3:
        return 0.0

    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)

    return abs(area) / 2