from settings import *

class Camera(pg.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.w = CAMERA_OFFSET[0]+PLAYER_SIZE[0]
        self.h = CAMERA_OFFSET[1]+PLAYER_SIZE[1]

        surf = pg.Surface((self.w,self.h),pg.SRCALPHA)
        #surf.fill((255,255,255))
        self.image = surf
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image,(255,255,255,50),self.rect.center,self.w//2)
        pg.draw.circle(self.image,(255,255,255,150),self.rect.center,self.w//3)
        pg.draw.circle(self.image,(255,255,255,200),self.rect.center,self.w//4)

    

    

    

    
