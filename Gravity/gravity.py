import pygame.gfxdraw
import math
from turtle import Screen
import pygame
pygame.init()

WHITE = (250, 250, 250)
BLACK = (5, 5, 5)

WIDTH = 1000
HEIGHT = 600

SCREEN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gravity')
SCREEN.fill(WHITE)


class Ball:
    def __init__(self, radius, center):
        self.radius = radius
        self.x = center[0]
        self.y = center[1]
        self.time = 0


balls = []

def draw_balls():
    for ball in balls:
        pygame.gfxdraw.aacircle(SCREEN, math.ceil(ball.x), math.ceil(ball.y), ball.radius, BLACK)

def fall():
    for ball in balls:
        g = 9.8
        h = 0.5*g*(ball.time)**2
        if ball.y + h + ball.radius > HEIGHT:
            ball.y = ball.y + (h - (ball.y + h + ball.radius - HEIGHT))
        else:
            ball.y = ball.y + h

RUNNING = True

clock = pygame.time.Clock()
frames = 1

while RUNNING:
    SCREEN.fill(WHITE)
    fall()
    draw_balls()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.mouse.get_pos()
            ball = Ball(25, center)
            balls.append(ball)

    for ball in balls:
        ball.time = ball.time + 1/frames
        
    pygame.display.update()
    clock.tick(frames)
            


pygame.quit()
