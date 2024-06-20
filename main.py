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

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        ICON = pg.image.load("2D Pixel Dungeon Asset Pack/Character_animation/monsters_idle/skull/v2/skull_v2_3.png")
        pg.Surface.convert_alpha(ICON)
        print(ICON)
        pg.display.set_icon(ICON)

        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 10)

        self.load()
    
    def load(self):
        game_dir = path.dirname(__file__)
        self.map = Map(path.join(game_dir, 'map.txt'))

    def new_instance(self):
        self.all_sprites = pg.sprite.Group()
        self.wall = pg.sprite.Group()

        ## not a big fan of this aproch to adding player or walls
        ## id prefer a map and then add the player on top of that
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == '*':
        #             wall(self, col, row)
        #         elif tile == 'p':
        #             self.player = Player(self, col, row)

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()
        
    def quit(self):
        pg.quit()
        sys.exit()
    
    def update(self):
        self.all_sprites.update()
    
    def events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.quit()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, BLACK, (x,0), (x,HEIGHT))
        
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, BLACK, (0,y), (WIDTH, y))

    def draw(self):
        self.screen.fill(TAN)
        self.draw_grid()
        self.all_sprites.draw(self.screen)

        # flip display after drawing
        pg.display.flip()


if __name__ == "__main__":
    g = Game()

    while True:
        g.new_instance()
        g.run()