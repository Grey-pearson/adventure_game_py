import pygame as pg
import sys
from os import path

from settings import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)
            
        n_horiz_tiles = len(self.data[0])
        n_vert_tiles = len(self.data)

        self.width = n_horiz_tiles*TILESIZE
        self.height = n_vert_tiles*TILESIZE

class Game:
    def __init__(self):
        pg.init()

        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 10)
        pg.display.set_icon(ICON)
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.load()
    
    def load(self):
        game_dir = path.dirname(__file__)
        self.map = Map(path.join(game_dir, 'map.txt'))

    def new_instance(self):
        self.all_sprites = pg.sprite.Group()
        self.wall = pg.sprite.Group()

        