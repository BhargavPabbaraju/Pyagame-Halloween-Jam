import pygame as pg
from spritesheet import Spritesheet
pg.init()

WIDTH =960
HEIGHT = 640
SIZE = 16

window = pg.display.set_mode((WIDTH,HEIGHT+128))


COLORS = [(255,255,0),(0,0,255)]
OPTIONSLIST = [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]
OPTIONS=[]
OPTIONSPOS=[]
GRID = [[]]


sheet = Spritesheet(".venv\\title\Images\walls.png")

for option in OPTIONSLIST:
    OPTIONS.append(sheet.get_sprite(*option,SIZE,SIZE))


selected = OPTIONS[0]

def grid():
    rows = HEIGHT // SIZE
    columns = WIDTH // SIZE
    k=1
    for c in range(columns):
        for r in range(rows):
            surf = pg.Surface((SIZE,SIZE))
            surf.fill(COLORS[k])
            
            pg.draw.rect(window,COLORS[k],[c*SIZE,r*SIZE,SIZE,SIZE])
            k=(k+1)%2

        k=(k+1)%2


def display_options():
    global OPTIONSPOS
    x=0
    y=640
    for option in OPTIONS:
        window.blit(option,(x,y))
        x+=SIZE
        OPTIONSPOS.append([x//SIZE,y//SIZE])
    
    

def click_checks():
    global selected
    mx,my = pg.mouse.get_pos()
    clicks = pg.mouse.get_pressed()
    if clicks[0]:
        for i in range(len(OPTIONS)):
            if [mx,my] == OPTIONSPOS[i]:
                selected = OPTIONS[i]
        
        


def draw():
    grid()
    display_options()






def loop():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()


        window.fill(-1)
        draw()
        click_checks()
        pg.display.update()



loop()

        
