import pygame
import pygame_gui
from bezier import bezier_curve
from draw import draw_curve
from utils import bezier_length

# Inicializálás
pygame.init()

WIDTH, HEIGHT = 900, 700
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bezier-görbe")
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Alapértelmezett kontrollpontok
control_points = [
    (CENTER_X - 200, CENTER_Y + 100),
    (CENTER_X, CENTER_Y - 200),
    (CENTER_X + 200, CENTER_Y + 100)
]
default_points = list(control_points)
selected_point = None
steps = 500

# Panel
panel = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((10, 10), (200, 180)),
    manager=manager
)

# Imput mező és gombok
steps_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 5), (180, 20)),
    text="Interpolációs pontok:",
    manager=manager,
    container=panel
)

steps_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((10, 30), (180, 30)),
    manager=manager,
    container=panel
)
steps_input.set_text(str(steps))

update_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 70), (180, 30)),
    text='Frissít',
    manager=manager,
    container=panel
)

reset_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 110), (180, 30)),
    text='Visszaállítás',
    manager=manager,
    container=panel
)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pont mozgatása
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, point in enumerate(control_points):
                    if pygame.Rect(point[0] - 5, point[1] - 5, 10, 10).collidepoint(event.pos):
                        selected_point = i
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected_point = None

        elif event.type == pygame.MOUSEMOTION and selected_point is not None:
            control_points[selected_point] = event.pos

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == update_button:
                    try:
                        steps = int(steps_input.get_text())
                    except ValueError:
                        steps = 500
                elif event.ui_element == reset_button:
                    control_points = list(default_points)

        manager.process_events(event)

    manager.update(time_delta)

    # Bézier görbe újraszámolása
    curve = bezier_curve(control_points, steps)
    length = bezier_length(curve)

    screen.fill((30, 30, 30))

    # Kontrollpontok közti vonalak
    for i in range(len(control_points) - 1):
        pygame.draw.line(screen, (100, 100, 255), control_points[i], control_points[i + 1], 1)

    # Bézier görbe
    if len(curve) > 1:
        draw_curve(screen, curve)

    # Kontrollpontok
    for point in control_points:
        pygame.draw.circle(screen, (255, 0, 0), point, 5)

    # Görbe hossza
    length_text = font.render(f"Görbe hossza: {round(length, 2)} px", True, (255, 255, 255))
    screen.blit(length_text, (10, HEIGHT - 30))

    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()