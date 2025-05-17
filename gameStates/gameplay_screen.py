import pygame
import config
from gameObjects.player import Player
from gameObjects.foods import FallingObject

player_instance = None
squares_list = []
current_score = 0
square_spawn_timer = 0
player_health = 100
falling_object_png_green = None
falling_object_png_red = None
falling_object_png_white = None
player_png_image = None
background_image = NotImplemented


score_font = None
esc_info_font = None
hp_font = None

def initialize_fonts():
    global score_font, esc_info_font, hp_font
    score_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_MEDIUM)
    esc_info_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_XSMALL)
    hp_font = pygame.font.Font(config.FONT_DEFAULT_NAME, config.FONT_SIZE_SMALL)

def reset_game_state(png_image_green, png_image_red, png_image_white, player_image, background):
    global player_instance, squares_list, current_score, square_spawn_timer, player_health, falling_object_png_green, falling_object_png_red, falling_object_png_white, player_png_image, background_image
    background_image = background
    player_png_image = player_image
    player_instance = Player(config.PLAYER_START_X, config.PLAYER_START_Y,
                                    0, config.PLAYER_SPEED, config.PLAYER_COLOR, player_image) 
    squares_list = []
    current_score = 0
    square_spawn_timer = 0
    player_health = 100
    falling_object_png_green = png_image_green
    falling_object_png_red = png_image_red
    falling_object_png_white = png_image_white
    if score_font is None: 
        initialize_fonts()
    print("Game play state reset and initialized.")

def handle_input(keys_map):
    if player_instance:
        player_instance.move(keys_map)

def update_game_logic():
    global square_spawn_timer, current_score, player_health 

  
    square_spawn_timer += 1
    if square_spawn_timer >= config.FALLING_OBJECT_SPAWN_RATE:
        square_spawn_timer = 0
        squares_list.append(FallingObject.spawn_random(falling_object_png_green, falling_object_png_red, falling_object_png_white)) 

    
    for falling_object in squares_list: 
        falling_object.move()

   
    if player_instance:
        player_center, player_radius = player_instance.get_collision_params()

    
        for i in range(len(squares_list) - 1, -1, -1):
            falling_object = squares_list[i]

          
            closest_x = max(falling_object.rect.left, min(player_center[0], falling_object.rect.right))
            closest_y = max(falling_object.rect.top, min(player_center[1], falling_object.rect.bottom))
            distance_squared = (player_center[0] - closest_x)**2 + (player_center[1] - closest_y)**2

            if distance_squared < (player_radius**2):
                squares_list.pop(i)
                if falling_object.type == 'color':
                    if falling_object.data == config.COLOR_GREEN:
                        current_score += 20
                        player_health = min(100, player_health + 5)
                    elif falling_object.data == config.COLOR_RED:
                        current_score -= 10
                        player_health = max(0, player_health - 10)
                    elif falling_object.data == config.COLOR_WHITE:
                        current_score += 10
                elif falling_object.type == 'image':
                   
                    if falling_object.data is falling_object_png_green:
                        current_score += 20
                        player_health = min(100, player_health + 5)
                    elif falling_object.data is falling_object_png_red:
                        current_score -= 10
                        player_health = max(0, player_health - 10)
                    elif falling_object.data is falling_object_png_white:
                        current_score += 10
                continue 

           
            if falling_object.is_off_screen():
                squares_list.pop(i)

def draw_screen(surface):
    global background_image
    if background_image:
        surface.blit(background_image, (0, 0))
    else:
        surface.fill(config.BLACK) 

    
    if esc_info_font:
        esc_text_render = esc_info_font.render("Press ESC for Menu", True, config.TEXT_COLOR_INGAME_INFO)
        esc_text_rect = esc_text_render.get_rect(center=(config.SCREEN_WIDTH // 2, 20))
        surface.blit(esc_text_render, esc_text_rect)

  
    if hp_font:
        hp_text_render = hp_font.render(f"HP: {player_health}/100", True, config.TEXT_COLOR_INGAME_INFO)
        surface.blit(hp_text_render, (10, 40))

  
    if player_instance and player_png_image:
        player_instance.draw(surface)

   
    for falling_object in squares_list:
        falling_object.draw(surface)

  
    if score_font:
        score_text_render = score_font.render(f"Score: {current_score}", True, config.TEXT_COLOR_INGAME_INFO)
        surface.blit(score_text_render, (10, 10))