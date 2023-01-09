import pygame
import menu


pygame.init()

size = width, height = 720, 480

screen = pygame.display.set_mode(size)

points = 0

font = pygame.font.Font(None, 48)

menu = menu.Menu(screen, font)
menu.start_menu()


