import pygame as pg
# file = "2D Pixel Dungeon Asset Pack/character and tileset/Dungeon_Tileset.png"

# class Game:
#     W = 160
#     H = 160
#     SIZE = W, H

pg.init()
win = pg.display.set_mode((500, 400))
pg.display.set_caption("visual sorter")
x = 40
y = 40

width = 40
# come up with a different way to create random stats, using random ig, 
# height = [10,20,30,40,50,60,70,80,90,100,110,120,130,140]
height = [ 20,
 10,
 30,
140,
 80,
 70,
 90,
110,
100,
130,
150,
 50,
 60,
 40,
120,]

# whats this do?
run = True

def show(height):
    for i in range(len(height)):
        pg.draw.rect(win, (255,0,0), (x+30*i, y, width, height[i]))
    
while run:
    execute = False
    pg.time.delay(10)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
    if keys[pg.K_SPACE]:
        execute = True
    if execute == False:
        win.fill((0,0,0))
        show(height)
        pg.display.update()
    
    else:
        for i in range(len(height)-1):
            for j in range(len(height)-1):
                if height[j] > height[j+1]:
                    t = height[j]
                    height[j] = height[j+1]
                    height[j+1] = t
                win.fill((0,0,0))
                show(height)
                pg.time.delay(50)
                pg.display.update()
                
pg.quit()
