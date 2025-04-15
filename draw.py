import pygame

def draw_curve(surface, curve_points, color=(255, 255, 0), width=2):
    if len(curve_points) > 1:
        pygame.draw.lines(surface, color, False, curve_points, width)