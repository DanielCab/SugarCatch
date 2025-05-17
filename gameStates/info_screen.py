import pygame
import config
from gameObjects.button import Button


title_font = None
info_text_font = None
back_button = None

def initialize_ui():
    global title_font, info_text_font, back_button
    title_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_LARGE)
    info_text_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_SMALL)
    print("Info screen UI initialized.")

    back_button = Button(
        "Back to Menu",
        config.SCREEN_WIDTH // 2 - config.BUTTON_BACK_WIDTH // 2, config.SCREEN_HEIGHT - 100,
        config.BUTTON_BACK_WIDTH, config.BUTTON_BACK_HEIGHT,
        config.GRAY, config.LIGHT_GRAY, action=config.STATE_MAIN_MENU
    )

def handle_input(event):
    if back_button:
        action = back_button.handle_event(event)
        return action
    return None

def draw_screen(surface):
    surface.fill(config.INFO_BG_COLOR) 

    if title_font is None or back_button is None or info_text_font is None:
        print("Warning: Info screen drawing before UI fully initialized.")
        return

    if title_font:
        title_render = title_font.render("Information", True, config.WHITE)
        title_rect = title_render.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 4))
        surface.blit(title_render, title_rect)

    if info_text_font:
        info_text = [
            "Welcome to SugarCatch",
            "The game consist of different obtainable foods",
            "that impact your health, score and speed!.",
            " ",
            "Move with A + D",
            "Group Members:",
            "Daniel Cabrices, Justine Ellis, AJ Durga, Ernest Jack",
            "Made as part of ITEC160 Final Project CRN 24304"
        ]
        y_offset = config.SCREEN_HEIGHT // 2 - 50
        for line in info_text:
            text_render = info_text_font.render(line, True, config.WHITE)
            text_rect = text_render.get_rect(center=(config.SCREEN_WIDTH // 2, y_offset))
            surface.blit(text_render, text_rect)
            y_offset += 30

    if back_button:
        back_button.draw(surface)