import pygame


class GameObject:

    def __init__(self, x, y, rect: pygame.Rect):
        self.rect = rect
        self.x = x
        self.y = y
        self.__update()

    def move(self, x, y):
        self.x += x
        self.y += -y
        self.__update()

    def __update(self):
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
