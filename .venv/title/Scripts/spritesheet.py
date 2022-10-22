
from settings import *

class SpriteSheet(pg.sprite.Sprite):
    def __init__(self,sheet):
        super().__init__()
        self.sheet = pg.image.load(sheet).convert_alpha()
       

    def get_sprite(self,x,y,w,h,scale):
        surface = pg.Surface((w,h))
        surface.blit(self.sheet,[x,y,w,h])
        surface = pg.transform.scale(surface,(w*scale,h*scale))
        return surface
    
