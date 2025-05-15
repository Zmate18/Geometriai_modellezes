import pygame
import pygame_gui

def create_ui_panel(manager):
    """
    Létrehozza az oldalsó vezérlőpanelt és annak UI elemeit.

    Paraméterek:
        manager (UIManager): A pygame_gui által használt kezelő, ami felelős a UI elemek kezeléséért.

    Visszatérési érték:
        tuple: Egy négy elemű tuple, ami tartalmazza:
            - panel (UIPanel): A fő konténer panel.
            - steps_input (UITextEntryLine): Szövegbeviteli mező az interpolációs pontok számának megadásához.
            - update_button (UIButton): Gomb, ami frissíti a görbét az új érték alapján.
            - reset_button (UIButton): Gomb, ami visszaállítja a kontrollpontokat az alapértelmezettre.
    """
    panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((10, 10), (200, 180)),
        manager=manager
    )

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
    steps_input.set_text("500")

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

    return panel, steps_input, update_button, reset_button