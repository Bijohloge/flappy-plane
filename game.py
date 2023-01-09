import random
import sys

import pygame

import cube
import pipes


class Game:

    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.background = pygame.image.load("background.png").convert()
        pipes.load_pipes()
        self.font = font
        self.cube = cube.Cube(40, 40)
        self.clock = pygame.time.Clock()
        self.pipe = []
        self.del_pipe = list()
        self.points = 0
        self.game_is_playing = True

    def remove_pipes(self):
        for p in self.del_pipe :
            self.pipe.remove(p)
        self.del_pipe.clear()

    def check_for_end(self):
        if self.cube.rect.y < 0 or self.cube.rect.y > self.screen.get_size()[1]:
            self.game_is_playing = False
        for p in self.pipe:
            if self.cube.rect.colliderect(p.rect):
                self.game_is_playing = False

    def spawn_pipes(self):
        height1 = random.randint(1, 12)
        height2 = 12 - height1

        self.pipe.append(pipes.Pipe(720 - 64, 0, height1, False))
        self.pipe.append(pipes.Pipe(720 - 64, 480 - height2 * 16, height2, True))
        pass

    def check_for_points(self, p: pipes.Pipe):
        if not p.isPassed:
            if p.x < self. cube.x:
                p.isPassed = True
                self.points += 1

    def run_game(self) -> int:
        pygame.time.set_timer(pygame.USEREVENT, 4000, 100)
        text = self.font.render(str(self.points), 1, (200, 200, 200))
        pos = text.get_rect()
        cooldown = 0

        while self.game_is_playing:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    self.spawn_pipes()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if cooldown < 1:
                    cooldown = 30
                pass

            text = self.font.render(str(int(self.points / 2)), 1, (200, 200, 200))

            if cooldown > 10:
                self.cube.move(0, cooldown * 0.4)
            else:
                self.cube.tick(self.clock.get_time() / 1000.0)
                pass
            if cooldown > 0:
                cooldown -= 1

            self.screen.blit(self.background, (0, 0))
            self.remove_pipes()

            for x in self.pipe:
                # pygame.draw.rect(screen, (255, 0, 0), x.rect)
                x.move(-1, 0)
                self.check_for_points(x)
                if x.x < -64:
                    self.del_pipe.append(x)
                x.render(self.screen)

            self.screen.blit(self.cube.image, self.cube.rect)
            self.screen.blit(text, pos)
            # pygame.draw.rect(screen, (255, 0, 0), cube.rect)
            self.check_for_end()
            pygame.display.update()
        return self.points
