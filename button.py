import pygame


class Button:

    def __init__(self, x, y, texture: pygame.Surface, text: str, font: pygame.font.Font):
        self.func = None
        self.rect = texture.get_rect().copy()
        self.texture = texture
        self.text = font.render(text, 1, (255, 255, 255))
        self.font = font
        self.rect.x = x
        self.rect.y = y
        self.text_rect = self.rect.copy()
        self.text_rect.x += self.rect.width / 2 - 25
        self.text_rect.y += self.rect.height / 2 - 25

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.texture, self.rect)
        screen.blit(self.text, self.text_rect)

    def add_listener(self, func):
        print(type(func))
        self.func = func
        print(type(self.func))


