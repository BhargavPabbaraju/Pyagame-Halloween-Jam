from settings import *
from camera import Camera

class Player(pg.sprite.Sprite):
    def __init__(self,game,x=100,y=100,speed=16,update_speed=100):
        super().__init__()
        surf = pg.Surface(PLAYER_SIZE)
        surf.fill((0,0,255))
        self.image = surf
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft =(x,y)
        self.speed = speed
        self.last_update = pg.time.get_ticks()
        self.update_speed = update_speed
        self.camera = Camera()
        self.camera.rect.center = self.rect.center
        self.game = game
        self.game.camera.add(self.camera)
        
    


    def check_moves(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.y-=self.speed
        
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.y+=self.speed
        
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.x-=self.speed
        
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.x+=self.speed


        self.rect.topleft = (self.x,self.y)
        self.camera.rect.center = self.rect.center

        
    
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.update_speed:
            self.check_moves()
            self.last_update = now
    
