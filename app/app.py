import pygame
import pygame_gui
from core.bezier import bezier_curve
from core.draw import draw_curve
from core.utils import bezier_length, estimate_area
from app.handlers import handle_events
from app.ui import create_ui_panel
from app import config

class App:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = config.WIDTH, config.HEIGHT
        self.CENTER_X, self.CENTER_Y = config.CENTER_X, config.CENTER_Y

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Bezier görbe")

        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

        self.control_points = list(config.DEFAULT_CONTROL_POINTS)
        self.default_points = list(config.DEFAULT_CONTROL_POINTS)
        self.selected_point = None
        self.steps = config.DEFAULT_STEPS

        self.panel, self.steps_input, self.update_button, self.reset_button = create_ui_panel(self.manager)
        self.running = True

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                self.running = handle_events(
                    event,
                    self.control_points,
                    self.default_points,
                    self.steps_input,
                    self.update_button,
                    self.reset_button,
                    self.manager,
                    self
                )

            self.manager.update(time_delta)
            self.render()

        pygame.quit()

    def render(self):
        curve = bezier_curve(self.control_points, self.steps)
        length = bezier_length(curve)
        closed_curve = curve + [curve[0]]
        area = estimate_area(closed_curve)

        self.screen.fill(config.BACKGROUND_COLOR)

        for i in range(len(self.control_points) - 1):
            pygame.draw.line(self.screen, config.CONTROL_LINE_COLOR, self.control_points[i], self.control_points[i + 1], 1)

        if len(curve) > 1:
            draw_curve(self.screen, curve)

        pygame.draw.polygon(self.screen, config.AREA_COLOR, closed_curve, 0)

        for point in self.control_points:
            pygame.draw.circle(self.screen, config.CONTROL_POINT_COLOR, point, 5)

        length_text = self.font.render(f"Görbe hossza: {round(length, 2)} px", True, config.TEXT_COLOR)
        self.screen.blit(length_text, (10, self.HEIGHT - 30))

        area_text = self.font.render(f"Közelítő terület: {round(area)} px²", True, config.TEXT_COLOR)
        self.screen.blit(area_text, (10, self.HEIGHT - 55))

        self.manager.draw_ui(self.screen)
        pygame.display.flip()