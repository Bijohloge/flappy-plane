import gameobject
import pygame

import pipes

pipes_images = None


def load_pipes():
    pipes.pipes_images = [pygame.transform.scale(pygame.image.load("pipe_top.png").convert(), (64, 32)),
                          pygame.transform.scale(pygame.image.load("pipe_bottom.png").convert(), (64, 32)),
                          pygame.transform.flip(
                              pygame.transform.scale(pygame.image.load("pipe_top.png").convert(), (64, 32)),
                              False, True)]


class Pipe(gameobject.GameObject):
    def __init__(self, x, y, height, isFlipped):
        rect = pygame.Rect((x, y), (64, 16 * height + 16))
        self.height = height
        self.isFlipped = isFlipped
        self.isPassed = False
        super().__init__(x, y, rect)

    def render(self, screen: pygame.surface.Surface):
        if self.isFlipped:
            screen.blit(pipes_images[0], self.rect)
            if self.height < 2:
                return
            for x in range(self.height - 1):
                move = self.rect.move(0, (x + 1) * 16)
                screen.blit(pipes_images[1], move)
        else:
            if self.height < 2:
                screen.blit(pipes_images[2], self.rect)
                return
            screen.blit(pipes_images[2], self.rect.move(0, (self.height - 1) * 16))
            for x in range(self.height - 1):
                move = self.rect.move(0, x * 16)
                screen.blit(pipes_images[1], move)
