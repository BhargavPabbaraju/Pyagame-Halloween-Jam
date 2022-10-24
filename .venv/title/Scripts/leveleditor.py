

from tkinter import W
from settings import *
from spritesheet import Spritesheet


path = '.venv\\title\Data\level'


class Level:
    def __init__(self,no):
        self.walls=pg.sprite.Group()
        self.doors = pg.sprite.Group()
        self.collectibles = pg.sprite.Group()
        self.no = no
        self.playercords=(0,0)
        self.make_level()
        


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
                    for wall in walls:
                        w = Wall(wall)
                        self.walls.add(w)
                elif n==5: # Doors
                    doors = eval(lines[n])
                    for door in doors:
                        d = Door(door)
                        self.doors.add(d)
                
                elif n==7: #Collectibles
                    collecs = eval(lines[n])
                    for collec in collecs:
                        c = Collectible(collec)
                        self.collectibles.add(c)

                   



class Wall(pg.sprite.Sprite):
    def __init__(self,pos,w=16,h=16):
        super().__init__()
        self.image = pg.Surface((w,h),pg.SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.pos = pos[0]*w ,pos[1]*h
        self.rect.topleft = self.pos
        #print(self.rect)


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
        self.sheet = Spritesheet('.venv\\title\Images\collectibles.png')
        self.load_image()
    

    def load_image(self):
        r,c=0,0
        if self.type == 'Torch':
            c=1
        
        self.image = self.sheet.get_sprite(r,c,self.w,self.h)
    

    def effect(self,game):
        if self.type == 'Key':
            game.has_key = True
            


