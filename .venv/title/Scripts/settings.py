import pygame as pg



WIDTH = 640
HEIGHT = 640

LEVEL = 1

PLAYER_SIZE = (16,32)
CAMERA_OFFSET = (64,64)
CAMERA_LERP_SPEED = 8
PLAYER_LERP_SPEED = 0.5

FPS = 60


FOG_COLOR = (0,0,0)


BGIMAGE = ".venv\\title\Images\\level"


pg.display.set_mode((WIDTH,HEIGHT))
pg.init()
clock = pg.time.Clock()
