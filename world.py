import pygame, sys, random

from constants import *
from particle import particle

pygame.init()
windowSize = (X_SIZE, Y_SIZE)
screen = pygame.display.set_mode(windowSize)
screen.fill(WHITE)
clock = pygame.time.Clock()


surface = pygame.Surface((X_SIZE,Y_SIZE), pygame.SRCALPHA)

gametime = 0
lastupdate = 0
smoke = []

while 1:
    surface.fill(WHITE)
    gametime = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in range(0, 20):
        p = particle(X_SIZE / 2, Y_SIZE - 20)
        smoke.append(p)

    for p in smoke:
        if p.tone == 0:
            smoke.remove(p)

        p.update()
        p.draw(surface)

    clock.tick()
    screen.blit(surface, (0,0))
    pygame.display.update()