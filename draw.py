import pygame

def draw_curve(surface, curve_points, color=(0, 255, 0), width=6):
    if len(curve_points) > 1:
        pygame.draw.lines(surface, color, False, curve_points, width)