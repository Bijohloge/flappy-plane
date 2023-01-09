import sys

import pygame.font

import button
import game


class Menu:

    def __init__(self, screen: pygame.surface.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.start_game = False
        self.points = 0
        self.buttons = list()
        self.button_image = pygame.image.load("button.png").convert()
        self.play_button = play_button = button.Button(260, 150, self.button_image.copy(), "Play", font)
        self.buttons.append(play_button)
        play_button.add_listener(self.run_game)
        self.quit_button = quit_button = button.Button(260, 300, self.button_image.copy(), "Quit", font)
        self.buttons.append(quit_button)
        self.score_text = self.font.render("Score: " + str(int(self.points / 2)), 1, (200, 200, 200))
        self.score_pos = self.score_text.get_rect()
        self.score_pos.x = 310
        self.score_pos.y = 80

    def run_game(self):
        self.start_game = True

    def is_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        is_clicked = pygame.mouse.get_pressed()
        if is_clicked[0]:
            for b in self.buttons:
                if b.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    b.func()

    def start_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.is_button_clicked()
            if self.start_game:
                new_game = game.Game(self.screen, self.font)
                self.points = new_game.run_game()

                self.start_game = False
            self.screen.fill((0, 0, 0))
            self.score_text = self.font.render("Score: " + str(int(self.points / 2)), 1, (200, 200, 200))
            self.quit_button.render(self.screen)
            self.play_button.render(self.screen)
            self.screen.blit(self.score_text, self.score_pos)
            pygame.display.flip()
