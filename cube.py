import pygame
import gameobject


class Cube(gameobject.GameObject):

    def __init__(self, x, y):
        self.image = pygame.image.load("cube.png")
        super().__init__(x, y, self.image.get_rect())


    def tick(self, delta):
        self.move(0, delta * -10 * 32)
