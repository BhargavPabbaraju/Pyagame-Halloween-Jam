
from settings import *

class Spritesheet(pg.sprite.Sprite):
    def __init__(self,sheet):
        super().__init__()
        self.sheet = pg.image.load(sheet).convert_alpha()
       

    def get_sprite(self,r,c,w,h,scale=1):
        surface = pg.Surface((w,h),pg.SRCALPHA)
        surface.blit(self.sheet,(0,0),[w*c,h*r,w,h])
        surface = pg.transform.scale(surface,(w*scale,h*scale))
        return surface
    
