import pygame
import pygame_gui

def handle_events(event, control_points, default_points, steps_input, update_button, reset_button, manager, app):
    """
    Kezeli az eseményeket az alkalmazásban.

    Paraméterek:
        event (pygame.event.Event): A Pygame által generált esemény.
        control_points (list of tuple): Az aktuális kontrollpontok listája.
        default_points (list of tuple): Az eredeti, visszaállítható kontrollpontok listája.
        steps_input (UITextEntryLine): Szövegbeviteli mező az interpolációs pontok számának megadásához.
        update_button (UIButton): A frissítés gomb (újraszámolja a görbét).
        reset_button (UIButton): A visszaállítás gomb (visszaállítja az alapértelmezett pontokat).
        manager (UIManager): A pygame_gui eseménykezelő és UI kezelő példánya.
        app (App): Az alkalmazás példánya, ami tárolja az állapotokat.

    Visszatérési érték:
        bool: False, ha a kilépés eseménye (QUIT) történt, különben True.
    """
    if event.type == pygame.QUIT:
        return False

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for i, point in enumerate(control_points):
            if pygame.Rect(point[0] - 5, point[1] - 5, 10, 10).collidepoint(event.pos):
                app.selected_point = i
                break

    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        app.selected_point = None

    elif event.type == pygame.MOUSEMOTION and app.selected_point is not None:
        control_points[app.selected_point] = event.pos

    if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == update_button:
            try:
                app.steps = int(steps_input.get_text())
            except ValueError:
                app.steps = 500
        elif event.ui_element == reset_button:
            app.control_points = list(default_points)

    manager.process_events(event)
    return True