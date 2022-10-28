

from tkinter import W
from settings import *
from spritesheet import Spritesheet
from random import randint

path = 'Data\level'


class Level:
    def __init__(self,no):
        self.walls=pg.sprite.Group()
        self.doors = pg.sprite.Group()
        self.collectibles = pg.sprite.Group()
        self.no = no
        self.playercords=(0,0)
        self.event_type = None
        self.make_level()
        self.last_update = pg.time.get_ticks()
        self.threshold = 1000 * randint(self.min_thres,self.max_thres)

        


    def make_level(self):
        with open(path+'%d.txt'%self.no) as file:
            lines = file.readlines()
            noOfLines = len(lines)
            for n in range(noOfLines):
                if n%2==0:
                    continue
                if n==1: #Playercords
                    self.playercords = eval(lines[n])
                elif n==3:#Walls cordinates
                    walls = eval(lines[n])
                    self.walls_list = walls
                    for wall in walls:
                        w = Wall(wall)
                        self.walls.add(w)
                elif n==5: # Events
                    event = eval(lines[n])
                    self.event_type = event[0]
                    self.min_thres = event[1]
                    self.max_thres = event[2]
                elif n==7: # Doors
                    doors = eval(lines[n])
                    for door in doors:
                        d = Door(door)
                        self.doors.add(d)
                
                elif n==9: #Collectibles
                    collecs = eval(lines[n])
                    for collec in collecs:
                        c = Collectible(collec)
                        self.collectibles.add(c)

    def time_passed(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.threshold:
            self.last_update = now
            return True
    

    def timeout(self,game):
        if self.event_type == 'DIE':
            
            game.shake_screen()
            game.play_sound("die")
            game.load_music("music 2")
            game.game_over(["YOU WERE SLASHED", "INTO PIECES!"])
            

        elif self.event_type=='BLOOD':
            game.bg=pg.image.load(BGIMAGE+'%d_blood.png'%self.no).convert_alpha()
            self.event_type='DIE'
            game.play_sound("shake")
            game.shake_screen()
            game.fade()
            self.last_update = pg.time.get_ticks()
            self.threshold = 1000 * randint(self.min_thres,self.max_thres)
           

        
                   



class Wall(pg.sprite.Sprite):
    def __init__(self,pos,w=16,h=16):
        super().__init__()
        self.image = pg.Surface((w,h),pg.SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.pos = pos[0]*w ,pos[1]*h
        self.rect.topleft = self.pos



class Door(pg.sprite.Sprite):
    def __init__(self,door,w=16,h=16):
        super().__init__()
        self.image = pg.Surface((w,h),pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.pos = pg.math.Vector2(door[0]*w ,door[1]*h)
        self.rect.topleft = self.pos
        self.to_level = door[2]
        self.to_cords = (door[3],door[4])
        self.locked = door[5]
        self.door = door
        


class Collectible(pg.sprite.Sprite):
    def __init__(self,collec,w=16,h=16):
        super().__init__()
        self.image = pg.Surface((w,h),pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.w = w
        self.h = h
        self.pos = pg.math.Vector2(collec[0]*w ,collec[1]*h)
        self.rect.topleft = self.pos
        self.type = collec[2]
        self.sheet = Spritesheet('.\Images\collectibles.png')
        self.load_image()
    

    def load_image(self):
        r,c=0,0
        if self.type == 'Torch':
            c=1
        
        self.image = self.sheet.get_sprite(r,c,self.w,self.h)
    

    def effect(self,game):
        if self.type == 'Key':
            game.has_key = True
            


