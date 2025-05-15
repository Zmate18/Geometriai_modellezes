import numpy as np

def de_casteljau(points, t):
    """
    Kiszámít egy pontot a Bézier görbén a de Casteljau algoritmussal.

    Paraméterek:
        points (list of tuple): A kontrollpontok listája.
        t (float): A paraméter 0 és 1 között, ami meghatározza, hogy a görbe melyik pontját számoljuk ki.

    Visszatérési érték:
        numpy.ndarray: A számított pont koordinátái a görbén.
    """
    points = np.array(points)
    n = len(points)
    for r in range(1, n):
        points = (1 - t) * points[:-1] + t * points[1:]
    return points[0]

def bezier_curve(control_points, steps=100):
    """
    Bézier görbét generál a megadott kontrollpontok alapján, adott felbontással.

    Paraméterek:
        control_points (list of tuple): A görbe kontrollpontjai.
        steps (int): Az interpoláció lépésszáma (minél nagyobb, annál simább a görbe).

    Visszatérési érték:
        list of tuple: A Bézier görbe pontjai.
    """
    return [de_casteljau(control_points, t) for t in np.linspace(0, 1, steps)]