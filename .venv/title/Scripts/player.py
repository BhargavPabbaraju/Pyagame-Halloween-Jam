from settings import *
from camera import Camera

from spritesheet import Spritesheet
player_sheet = Spritesheet(".venv\\title\Images\player.png")
class Player(pg.sprite.Sprite):
    def __init__(self,game,x=16,y=64,speed=16,update_speed=220):
        super().__init__()
        self.images = {'U':[],'D':[],'L':[],'R':[]}
        r=0
        for i in 'ULRD':
            for j in range(4):
                self.images[i].append(player_sheet.get_sprite(r,j,*PLAYER_SIZE))
            r+=1

        self.image = self.images['D'][0]
        self.rect = self.image.get_rect()
        self.pos = pg.math.Vector2(x,y)
        self.rect.topleft =self.pos
        self.speed = speed
        self.last_update = pg.time.get_ticks()
        self.update_speed = update_speed
        self.camera = Camera()
        self.camera.pos = pg.math.Vector2(self.rect.center)
        self.camera.rect.center = self.rect.center
        self.game = game
        self.game.camera.add(self.camera)
        self.turn = 0
        
    
    def change_image(self,direction):
        self.direction = direction
        self.turn = (self.turn+1)%4
        self.image = self.images[direction][self.turn]
    
    def can_move(self,xo,yo):
        rect = self.rect.copy()
        rect.x+=xo*self.speed
        rect.y+=yo*self.speed
        
        for wall in self.game.level.walls:
            if pg.Rect.colliderect(wall.rect,rect):
                return False
                #return False
        
        #ords = (self.rect.x//self.speed+xo,self.rect.y//self.speed+yo)

        return True
        
        

    def check_moves(self):
        

        keys = pg.key.get_pressed()
        
        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.can_move(0,-1):
                self.pos.y-=self.speed
                self.change_image('U')
            else:
                self.turn = 0
                self.image = self.images['U'][self.turn]
            
        
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            if self.can_move(0,1):
                self.pos.y+=self.speed
                self.change_image('D')
            else:
                self.turn = 0
                self.image = self.images['D'][self.turn]
            
        
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
             if self.can_move(-1,0):
                self.pos.x-=self.speed
                self.change_image('L')
             else:
                self.turn = 0
                self.image = self.images['L'][self.turn]
            
        
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.can_move(1,0):
                self.pos.x+=self.speed
                self.change_image('R')
            else:
                self.turn = 0
                self.image = self.images['R'][self.turn]
            


        self.rect.topleft = self.pos
        self.camera.apply(self.rect.center)

        
    
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.update_speed:
            self.check_moves()
            self.last_update = now
           
    
