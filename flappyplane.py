import pygame
import sys
import random

from pygame.surface import Surface, SurfaceType

import cube
from pipes import Pipe

pygame.init()

size = width, height = 720, 480

screen = pygame.display.set_mode(size)

points = 0

cube = cube.Cube(40, 40)
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 4000, 100)

font = pygame.font.Font(None, 36)
text = font.render(str(points), 1, (200, 200, 200))
pos = text.get_rect()

cooldown = 0

pipe = []


def spawn_pipes():
    height1 = random.randint(1, 12)
    height2 = 12 - height1

    pipe.append(Pipe(720 - 64, 0, height1, False))
    pipe.append(Pipe(720 - 64, 480 - height2 * 16, height2, True))
    pass


def check_for_points(p: Pipe, point: int):
    if not p.isPassed:
        if p.x < cube.x:
            p.isPassed = True
            point += 1
    return point


def check_for_end():
    if cube.rect.y < 0 or cube.rect.y > size[1]:
        sys.exit()
    for p in pipe:
        if cube.rect.colliderect(p.rect):
            sys.exit()


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT:
            spawn_pipes()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if cooldown < 1:
            cooldown = 30
        pass

    text = font.render(str(int(points / 2)), 1, (200, 200, 200))

    if cooldown > 10:
        cube.move(0, cooldown * 0.4)
    else:
        cube.tick(clock.get_time() / 1000.0)
        pass
    if cooldown > 0:
        cooldown -= 1

    screen.fill((0, 0, 0))

    for x in pipe:
        # pygame.draw.rect(screen, (255, 0, 0), x.rect)
        x.render(screen)
        x.move(-1, 0)
        points = check_for_points(x, points)
        if x.x < -64:
            pipe.remove(x)

    screen.blit(cube.image, cube.rect)
    screen.blit(text, pos)
    # pygame.draw.rect(screen, (255, 0, 0), cube.rect)
    check_for_end()
    pygame.display.update()
