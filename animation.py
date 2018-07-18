import pygame, sys, time
from pygame.locals import *

pygame.init()

W_WIDTH = 400
W_HEIGHT = 400
wSurface = pygame.display.set_mode((W_WIDTH, W_HEIGHT), 0, 32)
pygame.display.set_caption('Animation')

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir': UPLEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWNRIGHT}
blocks = [b1, b2, b3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    wSurface.fill(BLACK)

    for b in blocks:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

        if b['rect'].bottom > W_HEIGHT:
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT

        if b['rect'].left < 0:
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT

        if b['rect'].right > W_WIDTH:
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT

        pygame.draw.rect(wSurface, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(0.02)