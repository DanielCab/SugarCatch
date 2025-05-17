import pygame
import config
from gameObjects.button import Button


resume_button = None
options_button = None
info_button = None
quit_button = None
title_font = None
menu_buttons = []

def initialize_ui():
    global resume_button, options_button, info_button, quit_button, title_font, menu_buttons
    resume_button = Button(
        "Resume Game",
        config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 130,
        config.BUTTON_WIDTH, config.BUTTON_HEIGHT,
        config.GRAY, config.LIGHT_GRAY, action=config.STATE_GAME_PLAY
    )
    options_button = Button(
        "Options",
        config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 230,
        config.BUTTON_WIDTH, config.BUTTON_HEIGHT,
        config.GRAY, config.LIGHT_GRAY, action=config.STATE_OPTIONS
    )
    info_button = Button(
        "Info",
        config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 330,
        config.BUTTON_WIDTH, config.BUTTON_HEIGHT,
        config.GRAY, config.LIGHT_GRAY, action=config.STATE_INFO
    )
    quit_button = Button(
        "Quit Game",
        config.SCREEN_WIDTH // 2 - config.BUTTON_WIDTH // 2, 430,
        config.BUTTON_WIDTH, config.BUTTON_HEIGHT,
        config.INFO_BG_COLOR, config.LIGHT_GRAY, action="quit" 
    )
    menu_buttons = [resume_button, options_button, info_button, quit_button]
    title_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_LARGE)
    print("Menu screen UI initialized.")

def handle_input(event):
    for button in menu_buttons:
        action = button.handle_event(event)
        if action is not None:
            return action
    return None

def draw_screen(surface, draw_game_behind=False, game_surface=None):
    if draw_game_behind and game_surface:
        surface.blit(game_surface, (0,0)) 

    
    if draw_game_behind:
        dim_surface = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        dim_surface.fill((0, 0, 0, 150)) 
        surface.blit(dim_surface, (0, 0))
    else:
        surface.fill(config.WHITE) 

    if title_font:
        title_text_render = title_font.render("Paused", True, config.BLACK)
        title_rect = title_text_render.get_rect(center=(config.SCREEN_WIDTH // 2, 70))
        surface.blit(title_text_render, title_rect)

    for button in menu_buttons:
        button.draw(surface)