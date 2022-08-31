import pygame
import random


def transform(x,y):
    r = random.random()
    if r < 0.01:
        return 0.00 * x + 0.00 * y,  0.00 * x + 0.16 * y
    elif r < 0.86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y - 1.60
    elif r < 0.93:
        return 0.20 * x - 0.26 * y,  0.23 * x + 0.22 * y - 1.60
    else:
        return -0.15 * x + 0.28 * y,  0.26 * x + 0.24 * y - 0.44

def offset(n):
    return int((108*n)+1080)

pygame.init()

pygame.display.set_caption("Fern")
screen = pygame.display.set_mode((1920, 1080))
Running = True
x = 0
y = 0

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        Running = False

    x,y = transform(x,y)
    screen.set_at((offset(x),offset(y)),(0,255,0))

    pygame.display.flip()