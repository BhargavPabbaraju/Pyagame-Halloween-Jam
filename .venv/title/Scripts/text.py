
from re import X
from settings import *




class Textbox(pg.sprite.Sprite):
    def __init__(self,x=0,y=0,w=320,h=48):
        super().__init__()
        self.sheet = pg.image.load(TEXTBOXIMG).convert_alpha()
        self.font = pg.font.Font(FONTFILE,FONTSIZE)
        self.x = x
        self.w = w
        self.h = h
        self.y = self.w - self.h
        pg.font.init()
        self.change_text()
        self.active = False
        self.threshold = 700
        self.last_update = pg.time.get_ticks()
    

    def change_text(self,msg=""):
        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.image.blit(self.sheet,(0,0))
        self.rect = self.image.get_rect()
        surf = self.font.render(msg,True,(0,0,0))
        self.image.blit(surf,(12,12))
        self.rect.topleft = self.x,self.y
    

    def update(self):
        if not self.active:
            self.image=pg.Surface((0,0),pg.SRCALPHA)
        
        else:
            now = pg.time.get_ticks()
            if now - self.last_update > self.threshold:
                self.active = False
                self.last_update = now

        
