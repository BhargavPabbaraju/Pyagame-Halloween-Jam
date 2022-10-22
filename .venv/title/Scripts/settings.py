import pygame as pg



WIDTH = 640
HEIGHT = 640

LEVEL = 1

PLAYER_SIZE = (16,32)
CAMERA_OFFSET = (98,98)
CAMERA_LERP_SPEED = 0.4


FOG_COLOR = (0,0,0)


BGIMAGE = ".venv\\title\Images\\room.png"


pg.display.set_mode((WIDTH,HEIGHT))
pg.init()
clock = pg.time.Clock()
