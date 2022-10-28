import pygame as pg



WIDTH = 640
HEIGHT = 640

LEVEL = 1

PLAYER_SIZE = (16,32)
CAMERA_OFFSET = (64,64)
CAMERA_LERP_SPEED = 8
PLAYER_LERP_SPEED = 0.5

FPS = 60

FONTSIZE = 26
GAMEOVERFONTSIZE = 96
OPTIONSFONTSIZE = 48
INTROFONTSIZE = 48


FOG_COLOR = (0,0,0)


BGIMAGE = "Images\\level"
TEXTBOXIMG = 'Images\\textbox.png'
FONTFILE = 'who asks satan.ttf'
INTROBG = 'Images\introbg.png'
MUSICPATH = 'Audio\\'
PLAYERART = 'Images\\player art.png'


FINALLEVEL = 6


pg.display.set_mode((WIDTH,HEIGHT))
icon = pg.image.load('Images\\icon.png')
pg.display.set_icon(icon)
pg.display.set_caption("Reaper Mansion")
pg.init()
clock = pg.time.Clock()
