import pygame
import sys
import random

from pygame.surface import Surface, SurfaceType

import button
import cube
import flappyplane
import pipes
from pipes import Pipe

pygame.init()

size = width, height = 720, 480

screen = pygame.display.set_mode(size)

points = 0

background = pygame.image.load("background.png").convert()
button_image = pygame.image.load("button.png").convert()

pipes.load_pipes()

cube = cube.Cube(40, 40)
clock = pygame.time.Clock()


font = pygame.font.Font(None, 48)

buttons = list()

score_text = font.render("Score: " + str(int(points / 2)), 1, (200, 200, 200))
score_pos = score_text.get_rect()
score_pos.x = 310
score_pos.y = 80

game_is_playing = True




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
        flappyplane.game_is_playing = False
    for p in pipe:
        if cube.rect.colliderect(p.rect):
            flappyplane.game_is_playing = False


del_pipes = list()

pipe = []


def remove_pipes():
    for p in del_pipes:
        pipe.remove(p)
    del_pipes.clear()


def is_button_clicked():
    mouse_pos = pygame.mouse.get_pos()
    is_clicked = pygame.mouse.get_pressed()
    if is_clicked[0]:
        for b in buttons:
            if b.rect.collidepoint(mouse_pos[0], mouse_pos[1]):

                b.func()

def run_game():
    flappyplane.game_is_playing = True
    pygame.time.set_timer(pygame.USEREVENT, 4000, 100)
    text = font.render(str(points), 1, (200, 200, 200))
    pos = text.get_rect()
    cooldown = 0

    while flappyplane.game_is_playing:
        print(game_is_playing)
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

        font.render(str(int(points / 2)), 1, (200, 200, 200))

        if cooldown > 10:
            cube.move(0, cooldown * 0.4)
        else:
            cube.tick(clock.get_time() / 1000.0)
            pass
        if cooldown > 0:
            cooldown -= 1

        screen.blit(background, (0, 0))
        remove_pipes()

        for x in pipe:
            # pygame.draw.rect(screen, (255, 0, 0), x.rect)
            x.move(-1, 0)
            flappyplane.points = check_for_points(x, points)
            if x.x < -64:
                del_pipes.append(x)
            x.render(screen)

        screen.blit(cube.image, cube.rect)
        screen.blit(text, pos)
        # pygame.draw.rect(screen, (255, 0, 0), cube.rect)
        check_for_end()
        pygame.display.update()

play_button = button.Button(260, 150, button_image.copy(), "Play", font)
play_button.add_listener(run_game)
buttons.append(play_button)
quit_button = button.Button(260, 300, button_image.copy(), "Quit", font)
buttons.append(quit_button)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    is_button_clicked()
    print("--")
    screen.fill((0, 0, 0))
    score_text = font.render("Score: " + str(int(points / 2)), 1, (200, 200, 200))
    quit_button.render(screen)
    play_button.render(screen)
    screen.blit(score_text, score_pos)
    pygame.display.flip()
