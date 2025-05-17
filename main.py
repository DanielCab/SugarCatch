import pygame
import sys
import config
import time
from gameStates import gameplay_screen, menu_screen, options_screen, info_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Sugar Catch")
    clock = pygame.time.Clock()

    # Load images
    falling_object_png_image_green_scaled = None
    try:
        loaded_image_green = pygame.image.load(config.FALLING_OBJECT_PNG_PATH_GREEN).convert_alpha()
        falling_object_png_image_green_scaled = pygame.transform.scale(loaded_image_green, (config.FALLING_OBJECT_SIZE, config.FALLING_OBJECT_SIZE))
    except pygame.error as e:
        print(f"Error loading green image: {e}")
        sys.exit()

    falling_object_png_image_red_scaled = None
    try:
        loaded_image_red = pygame.image.load(config.FALLING_OBJECT_PNG_PATH_RED).convert_alpha()
        falling_object_png_image_red_scaled = pygame.transform.scale(loaded_image_red, (config.FALLING_OBJECT_SIZE, config.FALLING_OBJECT_SIZE))
    except pygame.error as e:
        print(f"Error loading red image: {e}")
        sys.exit()

    falling_object_png_image_white_scaled = None
    try:
        loaded_image_white = pygame.image.load(config.FALLING_OBJECT_PNG_PATH_WHITE).convert_alpha()
        falling_object_png_image_white_scaled = pygame.transform.scale(loaded_image_white, (config.FALLING_OBJECT_SIZE, config.FALLING_OBJECT_SIZE))
    except pygame.error as e:
        print(f"Error loading white image: {e}")
        sys.exit()

    player_png_image_scaled = None
    try:
        loaded_player_image = pygame.image.load(config.PLAYER_PNG_PATH).convert_alpha()
        player_png_image_scaled = pygame.transform.scale(loaded_player_image, (config.PLAYER_SIZE, config.PLAYER_SIZE))
    except pygame.error as e:
        print(f"Error loading player image: {e}")
        sys.exit()

    background_png_image = None
    try:
        loaded_background_image = pygame.image.load(config.BACKGROUND_PNG_PATH).convert()
        background_png_image = pygame.transform.scale(loaded_background_image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    except pygame.error as e:
        print(f"Error loading background image: {e}")
        sys.exit()

    # Initialize UI screens
    menu_screen.initialize_ui()
    options_screen.initialize_ui()
    info_screen.initialize_ui()

    current_state = config.STATE_GAME_PLAY
    gameplay_screen.reset_game_state(falling_object_png_image_green_scaled,
                                     falling_object_png_image_red_scaled,
                                     falling_object_png_image_white_scaled,
                                     player_png_image_scaled,
                                     background_png_image)

    paused_game_surface = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    running = True
    try:
        while running:
            keys_pressed = pygame.key.get_pressed()
            event = pygame.event.poll() 

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if current_state == config.STATE_GAME_PLAY and event.key == pygame.K_ESCAPE:
                    gameplay_screen.draw_screen(paused_game_surface)
                    current_state = config.STATE_MAIN_MENU
                elif current_state == config.STATE_MAIN_MENU and event.key == pygame.K_ESCAPE:
                    current_state = config.STATE_GAME_PLAY

            action = None
            if current_state == config.STATE_MAIN_MENU:
                action = menu_screen.handle_input(event)
            elif current_state == config.STATE_OPTIONS:
                action = options_screen.handle_input(event)
            elif current_state == config.STATE_INFO:
                action = info_screen.handle_input(event)

            if action:
                if action == "quit":
                    running = False
                elif action == config.STATE_GAME_PLAY:
                    current_state = action
                    gameplay_screen.reset_game_state(falling_object_png_image_green_scaled,
                                                     falling_object_png_image_red_scaled,
                                                     falling_object_png_image_white_scaled,
                                                     player_png_image_scaled,
                                                     background_png_image)
                elif action == config.STATE_OPTIONS:
                    options_screen.initialize_ui()
                    current_state = action
                elif action == config.STATE_INFO:
                    info_screen.initialize_ui()
                    current_state = action
                elif action == config.STATE_MAIN_MENU:
                    current_state = action

            if current_state == config.STATE_GAME_PLAY:
                gameplay_screen.handle_input(keys_pressed)
                gameplay_screen.update_game_logic()

            # Drawing
            if current_state == config.STATE_GAME_PLAY:
                gameplay_screen.draw_screen(screen)
            elif current_state == config.STATE_MAIN_MENU:
                menu_screen.draw_screen(screen, draw_game_behind=True, game_surface=paused_game_surface)
            elif current_state == config.STATE_OPTIONS:
                options_screen.draw_screen(screen)
            elif current_state == config.STATE_INFO:
                info_screen.draw_screen(screen)

            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()