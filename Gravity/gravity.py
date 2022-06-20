import math
import pygame
pygame.init()

WHITE = (250, 250, 250)
BLACK = (5, 5, 5)

SCREEN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gravity')
SCREEN.fill(WHITE)


class Ball:
    def __init__(self):
        self.radius = 50
        self.center = None


RUNNING = True

while RUNNING:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN, BLACK, pos, 50, 5)
            


pygame.quit()
