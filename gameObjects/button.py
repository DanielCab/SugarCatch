import pygame
import config 

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None, text_color=config.BUTTON_TEXT_COLOR, font_size=config.FONT_SIZE_LARGE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.text_color = text_color
        self.is_hovered = False
        self.font = pygame.font.Font(config.FONT_DEFAULT_NAME, font_size)

    def draw(self, surface):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(surface, config.BLACK, self.rect, 2) # Border

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1: # Left click
                if self.action is not None:
                    return self.action
        return None