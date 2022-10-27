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


BGIMAGE = ".venv\\reaper mansion\Images\\level"
TEXTBOXIMG = '.venv\\reaper mansion\Images\\textbox.png'
FONTFILE = '.venv\\reaper mansion\who asks satan.ttf'
INTROBG = '.venv\\reaper mansion\Images\introbg.png'
MUSICPATH = '.venv\\reaper mansion\Audio\\'


pg.display.set_mode((WIDTH,HEIGHT))
pg.init()
clock = pg.time.Clock()
