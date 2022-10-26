
from re import X
from settings import *




class Textbox(pg.sprite.Sprite):
    def __init__(self,x=0,y=0,w=320,h=48,fontsize=FONTSIZE):
        super().__init__()
        self.sheet = pg.image.load(TEXTBOXIMG).convert_alpha()
        self.font = pg.font.Font(FONTFILE,fontsize)
        self.x = x
        self.w = w
        self.h = h
        self.y = self.w - self.h
        pg.font.init()
        self.change_text()
        self.active = False
        self.threshold = 700
        self.last_update = pg.time.get_ticks()
    

    def change_text(self,msg="",alpha=False):
        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        if not alpha:
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

        


class OptionText(pg.sprite.Sprite):
    def __init__(self,option,color,index,game):
        super().__init__()
        self.active = False
        self.option = option
        self.index = index
        self.color = color
        self.make_image()
        self.game = game
    

    def make_image(self):
        font = pg.font.Font(FONTFILE,OPTIONSFONTSIZE)
        text = font.render(self.option,True,self.color)
        rect = text.get_rect()
        if self.index==0:
            rect.x = rect.width + 10
        else:
            rect.x = WIDTH - rect.width - 100
        rect.y = HEIGHT - OPTIONSFONTSIZE*2
        self.image = text
        self.rect = rect
    

    def update(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image.set_alpha(100)
            clicks = pg.mouse.get_pressed()
            if clicks[0]:
                self.click()
        else:
            self.image.set_alpha(255)
    

    def click(self):
        if self.option=='QUIT':
            pg.quit()
            quit()
        
        elif self.option == 'PLAY AGAIN':
            self.game.over_running = False
            self.game.game_running = True
            self.game.new_level(self.game.level.no)
            self.game.run()
            
        