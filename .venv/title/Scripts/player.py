from settings import *
from camera import Camera

from spritesheet import Spritesheet
player_sheet = Spritesheet(".venv\\title\Images\player.png")
class Player(pg.sprite.Sprite):
    def __init__(self,game,x=100,y=100,speed=16,update_speed=100):
        super().__init__()
        self.images = {'U':[],'D':[],'L':[],'R':[]}
        r=0
        for i in 'ULRD':
            for j in range(4):
                self.images[i].append(player_sheet.get_sprite(r,j,*PLAYER_SIZE,2))
            r+=1

        self.image = self.images['D'][0]
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
        self.turn = 0
        
    
    def change_image(self,direction):
        self.turn = (self.turn+1)%4
        self.image = self.images[direction][self.turn]

    def check_moves(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.y-=self.speed
            self.change_image('U')
            
        
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.y+=self.speed
            self.change_image('D')
        
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.x-=self.speed
            self.change_image('L')
        
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.x+=self.speed
            self.change_image('R')


        self.rect.topleft = (self.x,self.y)
        self.camera.rect.center = self.rect.center

        
    
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.update_speed:
            self.check_moves()
            self.last_update = now
    
