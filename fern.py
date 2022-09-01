import pygame
import random


def transform(x,y):
    r = random.random()
    if r < 0.01:
        a,b = 0,  0.16 * y
    elif r < 0.89:
        a,b = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y - 1.60
    elif r < 0.94:
        a,b = 0.20 * x - 0.26 * y,  0.23 * x + 0.22 * y - 1.60
    else:
        a,b = -0.15 * x + 0.28 * y,  0.26 * x + 0.24 * y - 0.44
    screen.set_at((int((108*a)+1080),int((108*b)+1080)),color)
    return a,b

def rc():
    return random.randint(0,255)

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

    color = (rc(),rc(),rc())
    #color = (0,255,0)

    for i in range(100000):
        x,y = transform(x,y)
        

    pygame.display.flip()