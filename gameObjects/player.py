import pygame
import config

class Player:
    def __init__(self, x, y, radius, speed, color, image=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.image = image
        if self.image is not None:
            self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def move(self, keys_map):
        if self.image is not None:
            if keys_map[pygame.K_a]:
                self.rect.x -= self.speed
            if keys_map[pygame.K_d]:
                self.rect.x += self.speed

            # Keep player within screen bounds
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > config.SCREEN_WIDTH:
                self.rect.right = config.SCREEN_WIDTH
            self.x = self.rect.centerx 
            self.y = self.rect.centery 
        else:
            if keys_map[pygame.K_a]:
                self.x -= self.speed
            if keys_map[pygame.K_d]:
                self.x += self.speed

            # Keep player within screen bounds
            if self.x - self.radius < 0:
                self.x = self.radius
            elif self.x + self.radius > config.SCREEN_WIDTH:
                self.x = config.SCREEN_WIDTH - self.radius
            self.rect.center = (int(self.x), int(self.y)) # Update rect's center

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, self.rect)
        else:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def get_collision_params(self):
        if self.image is not None:
            return self.rect.center, max(self.image.get_width(), self.image.get_height()) // 2 # Approximate radius
        else:
            return (int(self.x), int(self.y)), self.radius