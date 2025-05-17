import pygame
import random
import config

class FallingObject:
    def __init__(self, x, y, item_type, data, speed):
        self.type = item_type # 'color' or 'image'
        self.data = data      # Color tuple or pygame.Surface
        self.rect = self.get_rect(x, y)
        self.speed = speed

    def get_rect(self, x, y):
        if self.type == 'color':
            return pygame.Rect(x, y, config.FALLING_OBJECT_SIZE, config.FALLING_OBJECT_SIZE)
        elif self.type == 'image':
            return self.data.get_rect(topleft=(x, y))
        return None

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        if self.type == 'color':
            pygame.draw.rect(surface, self.data, self.rect)
        elif self.type == 'image':
            surface.blit(self.data, self.rect)

    def is_off_screen(self):
        return self.rect.top > config.SCREEN_HEIGHT

    @staticmethod
    def spawn_random(png_image_green, png_image_red, png_image_white):
        random_choice = random.choice(['red', 'green', 'white'])
        if random_choice == 'green':
            if png_image_green:
                obj_x = random.randint(0, config.SCREEN_WIDTH - png_image_green.get_width())
                obj_y = -png_image_green.get_height()
                return FallingObject(obj_x, obj_y, 'image', png_image_green, config.FALLING_OBJECT_SPEED)
            else:
                obj_x = random.randint(0, config.SCREEN_WIDTH - config.FALLING_OBJECT_SIZE)
                obj_y = -config.FALLING_OBJECT_SIZE
                return FallingObject(obj_x, obj_y, 'color', config.COLOR_GREEN, config.FALLING_OBJECT_SPEED)
        elif random_choice == 'red':
            if png_image_red:
                obj_x = random.randint(0, config.SCREEN_WIDTH - png_image_red.get_width())
                obj_y = -png_image_red.get_height()
                return FallingObject(obj_x, obj_y, 'image', png_image_red, config.FALLING_OBJECT_SPEED)
            else:
                obj_x = random.randint(0, config.SCREEN_WIDTH - config.FALLING_OBJECT_SIZE)
                obj_y = -config.FALLING_OBJECT_SIZE
                return FallingObject(obj_x, obj_y, 'color', config.COLOR_RED, config.FALLING_OBJECT_SPEED)
        elif random_choice == 'white':
            if png_image_white:
                obj_x = random.randint(0, config.SCREEN_WIDTH - png_image_white.get_width())
                obj_y = -png_image_white.get_height()
                return FallingObject(obj_x, obj_y, 'image', png_image_white, config.FALLING_OBJECT_SPEED)
            else:
                obj_x = random.randint(0, config.SCREEN_WIDTH - config.FALLING_OBJECT_SIZE)
                obj_y = -config.FALLING_OBJECT_SIZE
                return FallingObject(obj_x, obj_y, 'color', config.COLOR_WHITE, config.FALLING_OBJECT_SPEED)
        return None