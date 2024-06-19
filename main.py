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
    