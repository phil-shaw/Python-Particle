import pygame, random

from constants import *

class particle():


    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = random.randint(-1, 1)
        self.yvel = random.randint(-4, -2)
        self.tone = 255


    def update(self):

        if self.ypos <= 570:
            self.xvel += random.randint(-1, 1)

        self.xpos += self.xvel
        self.ypos += self.yvel
        self.tone -= 2

        if self.tone < 0:
            self.tone = 0


    def draw(self, surface):
        self.surface = surface

        pygame.draw.circle(surface, (0, 0, 0, self.tone), (int(self.xpos), int(self.ypos)), 4)

