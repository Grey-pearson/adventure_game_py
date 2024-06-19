import pygame, sys
from random import randrange
from pygame.locals import *
from settings import *

pygame.init()
fps = pygame.time.Clock()

pygame.display.set_icon(ICON)
surfObj = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)