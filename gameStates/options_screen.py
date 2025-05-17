import pygame
import config
from gameObjects.button import Button

# Options are completely decorational and have zero functionality :p

back_button = None
title_font = None
option_font = None


window_size_text = None
sound_text = None
window_size_rect = None
sound_slider_bg = None
sound_slider_indicator = None

def initialize_ui():
    global back_button, title_font, option_font
    global window_size_text, sound_text, window_size_rect, sound_slider_bg, sound_slider_indicator

    back_button = Button(
        "Back to Menu",
        config.SCREEN_WIDTH // 2 - config.BUTTON_BACK_WIDTH // 2, config.SCREEN_HEIGHT - 100,
        config.BUTTON_BACK_WIDTH, config.BUTTON_BACK_HEIGHT,
        config.GRAY, config.LIGHT_GRAY, action=config.STATE_MAIN_MENU
    )
    title_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_LARGE)
    option_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_MEDIUM)


    start_y = config.SCREEN_HEIGHT // 3
    vertical_spacing = 60

   
    window_size_text = option_font.render("Window Size:", True, config.WHITE)
    window_size_rect = window_size_text.get_rect(topleft=(config.SCREEN_WIDTH // 4 - window_size_text.get_width() // 2, start_y))

   
    sound_text = option_font.render("Sound Volume:", True, config.WHITE)
    sound_text_rect = sound_text.get_rect(topleft=(config.SCREEN_WIDTH // 4 - sound_text.get_width() // 2, start_y + vertical_spacing))
    sound_slider_bg = pygame.Rect(config.SCREEN_WIDTH // 4 - 75, sound_text_rect.bottom + 10, 150, 20)
    sound_slider_indicator = pygame.Rect(config.SCREEN_WIDTH // 4 - 50, sound_slider_bg.top, 20, 20)

    print("Options screen UI initialized.")

def handle_input(event):
    if back_button:
        action = back_button.handle_event(event)
        return action
    return None

def draw_screen(surface):
    global window_size_text, sound_text, window_size_rect, sound_slider_bg, sound_slider_indicator

    surface.fill(config.OPTIONS_BG_COLOR)

    if title_font:
        title_render = title_font.render("Options Menu", True, config.WHITE)
        title_rect = title_render.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 4 - 50))
        surface.blit(title_render, title_rect)

 
    if window_size_text and window_size_rect:
        surface.blit(window_size_text, (window_size_rect.left, window_size_rect.top))
        pygame.draw.rect(surface, config.GRAY, window_size_rect, 2)
        size_option_text = option_font.render("800x600 (Static)", True, config.LIGHT_GRAY)
        size_option_rect = size_option_text.get_rect(topleft=(window_size_rect.left, window_size_rect.bottom + 5)) # Position below
        surface.blit(size_option_text, size_option_rect)


    if sound_text and sound_slider_bg and sound_slider_indicator:
        surface.blit(sound_text, (sound_slider_bg.left, sound_slider_bg.top - option_font.get_height() - 5))
        pygame.draw.rect(surface, config.GRAY, sound_slider_bg)
        pygame.draw.rect(surface, config.LIGHT_GRAY, sound_slider_indicator)

    if back_button:
        back_button.draw(surface)