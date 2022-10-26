from settings import *
from camera import Camera

from spritesheet import Spritesheet
player_sheet = Spritesheet(".venv\\title\Images\player.png")
class Player(pg.sprite.Sprite):
    def __init__(self,game,x=1,y=4,speed=320,update_speed=100):
        super().__init__()
        self.get_images(player_sheet)

        self.image = self.images['D'][0]
        self.rect = self.image.get_rect()
        x*=PLAYER_SIZE[0]
        y*=PLAYER_SIZE[1]
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
        
        self.target = self.pos

    
    def get_images(self,sheet):
        self.images = {'U':[],'D':[],'L':[],'R':[]}
        r=0
        for i in 'ULRD':
            for j in range(4):
                self.images[i].append(sheet.get_sprite(r,j,*PLAYER_SIZE))
            r+=1
        

        
    
    def change_image(self,direction):
        self.direction = direction
        self.turn = (self.turn+1)%4
        self.image = self.images[direction][self.turn]
    
                
    

    def collisions(self,dx,dy):

        #self.target = pg.math.Vector2((self.pos.x+self.speed*dx,self.pos.y))
        #self.pos = self.pos.lerp(self.target,PLAYER_LERP_SPEED)
        #self.pos += pg.math.Vector2((self.speed*dx,0))
        #self.pos.x+=self.speed*dx
        self.rect.x+=self.speed*dx * self.game.dt

        for wall in self.game.level.walls:
            if pg.Rect.colliderect(wall.rect,self.rect):
                
                if dx==1:
                    self.rect.right = wall.rect.left
                else:
                    self.rect.left = wall.rect.right
                
                
        

        #self.target = pg.math.Vector2((self.pos.x,self.pos.y+self.speed*dy))
        #self.pos = self.pos.lerp(self.target,PLAYER_LERP_SPEED)
        #self.pos += pg.math.Vector2((0,self.speed*dy))
        self.rect.y+=self.speed*dy* self.game.dt


        for wall in self.game.level.walls:
            if pg.Rect.colliderect(wall.rect,self.rect):
                
                if dy==1:
                    self.rect.bottom = wall.rect.top
                else:
                    self.rect.top = wall.rect.bottom
        

        
                
        
        
        direction = {(1,0):'R',(0,1):'D',(-1,0):'L',(0,-1):'U'}
        self.change_image(direction[(dx,dy)])

        if direction[(dx,dy)] == 'U':
            for door in self.game.level.doors:
                if pg.Rect.colliderect(door.rect,self.rect):
                    if door.door in self.game.opened_doors:
                        self.game.textbox.active = True
                        self.game.textbox.change_text("This door is permanently locked.")
                        self.game.textbox.last_update = pg.time.get_ticks()
                    elif not door.locked:
                        self.open_door(door)
                        self.game.opened_doors.append(door.door)
                    elif self.game.has_key:
                        self.game.has_key = False
                        self.open_door(door)
                        self.game.opened_doors.append(door.door)
                    else:
                        self.game.textbox.active = True
                        self.game.textbox.change_text("You need a key to open this door.")
                        self.game.textbox.last_update = pg.time.get_ticks()
        

        for collec in self.game.level.collectibles:
            if pg.Rect.colliderect(collec.rect,self.rect):
                collec.effect(self.game)
                collec.kill()
                
                    
                    
        
        
    def open_door(self,door):
        self.game.fade()
        self.game.new_level(door.to_level,door.to_cords)
        self.kill()
    

    def die(self):
        sheet = Spritesheet(".venv\\title\Images\player blood.png")
        self.get_images(sheet)
        
        
        
                
                

                
            
                
    


    
        

    def check_moves(self):
        

        keys = pg.key.get_pressed()
        
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.collisions(0,-1)
            
                
        
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.collisions(0,1)
            
            
            
        
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.collisions(-1,0)
            
            
            
        
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            
            self.collisions(1,0)
        

        elif keys[pg.K_h]:
            self.game.debug = not self.game.debug
        
            

        
        
        

        
    
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.update_speed:
            self.check_moves()
            self.last_update = now
        
            self.camera.apply(self.rect.center,self.game.dt)
           
    
