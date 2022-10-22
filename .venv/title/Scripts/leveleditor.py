

from settings import *



path = '.venv\\title\Data\level'


class Level:
    def __init__(self,no):
        self.walls=pg.sprite.Group()
        self.no = no
        self.make_level()


    def make_level(self):
        with open(path+'%d.txt'%self.no) as file:
            lines = file.readlines()
            noOfLines = len(lines)
            for n in range(noOfLines):
                if n==0: #Walls
                    continue
                elif n==1:#Walls cordinates
                    walls = eval(lines[n])
                    for wall in walls:
                        w = Wall(wall)
                        self.walls.add(w)
                   



class Wall(pg.sprite.Sprite):
    def __init__(self,pos,w=16,h=16):
        super().__init__()
        self.image = pg.Surface((w,h),pg.SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.pos = pos[0]*w ,pos[1]*h
        self.rect.topleft = self.pos
        #print(self.rect)