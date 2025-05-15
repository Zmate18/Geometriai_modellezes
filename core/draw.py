import pygame
from app import config

def draw_curve(surface, curve_points):
    """
    Kirajzolja a Bézier görbét a megadott pontok alapján.

    Paraméterek:
        surface (pygame.Surface): Az a felület, amire a görbét rajzoljuk.
        curve_points (list of tuple): A Bézier görbe pontjai.
        color (tuple): A görbe színe.
        width (int): A vonal vastagsága.

        Csak akkor rajzol, ha legalább két pontból áll a görbe.
    """
    if len(curve_points) > 1:
        pygame.draw.lines(
            surface,
            config.CURVE_COLOR,
            False,
            curve_points,
            config.CURVE_WIDTH
        )