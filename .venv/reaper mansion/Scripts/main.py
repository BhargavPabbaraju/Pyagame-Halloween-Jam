from settings import *
from player import Player
from text import Textbox,OptionText,CreditText
from leveleditor import Level
from math import sin,cos



class Game:
    def __init__(self):
        self.screen = pg.Surface((WIDTH//2,HEIGHT//2))

        
        self.fog = pg.Surface((WIDTH,HEIGHT),pg.SRCALPHA)
        self.debug = False
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
        
        self.clock = pg.time.Clock()
        
        self.fade_out = True
        self.has_key = False
        self.opened_doors=[]
        self.game_running = False
        self.over_running = False
        self.menu_running = True
        self.persist_player_cords = False
        self.player_cords = (0,0)
        self.finish_running = False
        
        
    

    def new_level(self,lvl=1,cords=None):
        
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.camera = pg.sprite.Group()
        self.textbox = Textbox()
        

        self.level = Level(lvl)
        for collec in self.level.collectibles:
            self.all_sprites.add(collec)

        cords = self.level.playercords if not cords else cords
        if self.persist_player_cords:
            cords = self.player_cords
            

    
        self.player = Player(self,*cords)
        
        self.player_sprite.add(self.player)
        self.bg = pg.image.load(BGIMAGE+'%d.png'%self.level.no).convert_alpha()
        
        self.draw_screen()
        

    def draw_screen(self):
        self.screen.fill(1)
        self.screen.blit(self.bg,(0,0))
        
        
        self.all_sprites.draw(self.screen)
        

        if not self.debug:
            self.fog.fill(FOG_COLOR)
            self.camera.draw(self.fog)
            self.screen.blit(self.fog,(0,0),special_flags=pg.BLEND_MULT)
        else:
            self.camera.draw(self.screen)
        
        self.player_sprite.draw(self.screen)
        self.textbox.update()
        self.screen.blit(self.textbox.image,self.textbox.rect)
        

        if self.debug:
            pg.draw.rect(self.screen,(0,255,0),self.player.rect,width=2)
            for wall in self.level.walls:
                pg.draw.rect(self.screen,(255,0,0),wall.rect,width=2)
            for door in self.level.doors:
                pg.draw.rect(self.screen,(255,100,20),door.rect,width=2)


    def display_window(self):
        
        self.window.fill(1)
        surf = pg.transform.scale(self.screen,(WIDTH,HEIGHT))
        self.window.blit(surf,(0,0))
        #Draw walls
        
    
    def fade(self):
        
        if self.fade_out:
            self.draw_screen()
            self.display_window()
            surf = pg.Surface((WIDTH,HEIGHT))
            i = 0
            while i<50:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                
                
                
                surf.set_alpha(i)
                self.window.blit(surf,(0,0))
                pg.display.update()
                pg.time.delay(110)
                i+=5
                
        
        else:
            surf = pg.Surface((WIDTH,HEIGHT))
            surf.fill((100,100,100))
            i = 50
            while i>0:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                
                
                
                surf.set_alpha(i)
                self.display_window()
                self.window.blit(surf,(0,0))
                pg.display.update()
                pg.time.delay(110)
                i-=5
                
            
        self.fade_out = not self.fade_out
        

        
        
    def shake_screen(self):
        numberOfShakes = 20
        surf =  pg.transform.scale(self.screen,(WIDTH,HEIGHT))
        for i in range(numberOfShakes):
            speed = 10
            x=cos(pg.time.get_ticks()) * speed
            y=sin(pg.time.get_ticks()) * speed
            self.window.fill(1)
            self.window.blit(surf,(x,y))
            pg.display.flip()
            self.window.fill(1)
            self.window.blit(surf,(0,0))
            pg.time.delay(50)

    
    def game_over(self,msg):
        self.game_running = False
        self.over_running = True
        self.game_over_loop(msg)

    def event_checks(self):
        if self.level.time_passed():
            self.level.timeout(self)

    
    def display_game_over_text(self,msg):
        font = pg.font.Font(FONTFILE,GAMEOVERFONTSIZE)
        surf = pg.Surface((WIDTH,HEIGHT),pg.SRCALPHA)
        surf.fill((100,100,100,10))
        surfs=[]
        n=len(msg)
        for i in range(n):
            text = font.render(msg[i],True,(138,3,3))
            rect = text.get_rect()
            rect.center = surf.get_rect().center
            if n%2==1 and i==n/2:
                surf.blit(text,rect)
            else:
                if i<n/2:
                    rect.y-=GAMEOVERFONTSIZE//n
                else:
                    rect.y+=GAMEOVERFONTSIZE//n
                

                
                surf.blit(text,rect)
        
        
        return surf
    
    def display_options(self,options):
        self.options = pg.sprite.Group()
        for i in range(2):
            color = (255,0,0) if options[i] =='QUIT' else (255,255,255)
            self.options.add(OptionText(options[i],color,i,self))
        
    def game_over_loop(self,msg):
        self.player.die()
        self.player_sprite.update()
        self.textbox.active = False
        self.textbox.update()
        self.draw_screen()
        pg.time.delay(200)
        
        surf = self.display_game_over_text(msg)
        self.display_options(["QUIT","PLAY AGAIN"])
        
        

        while self.over_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            

            self.display_window()
            self.window.blit(surf,(0,0))
            self.options.update()
            self.options.draw(self.window)
            pg.display.flip()

    def run(self):
        
        self.load_music('music 3')
        while self.game_running:
            self.dt = self.clock.tick(FPS)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            
            self.event_checks()
            self.player_sprite.update()
            self.draw_screen()
            self.display_window()
            pg.display.update()
    

    def load_music(self,music):
        pg.mixer.music.stop()
        pg.mixer.music.load(MUSICPATH+music+'.wav')
        pg.mixer.music.play(-1)
    
    def play_sound(self,music):
        sound = pg.mixer.Sound(MUSICPATH+music+'.wav')
        sound.play()

    def menu_loop(self):
        
        introbg = pg.image.load(INTROBG).convert_alpha()
        font = pg.font.Font(FONTFILE,INTROFONTSIZE)
        text = font.render("Reaper Mansion",True,(138,3,3))
        rect = text.get_rect()
        rect.center = self.screen.get_rect().center
        rect.y = 32

        self.screen.blit(introbg,(0,64+16+8))
        self.screen.blit(text,rect)
        self.display_options(["PLAY","QUIT"])
        self.load_music('music 1')
        while self.menu_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            
            self.display_window()
            self.options.update()
            self.options.draw(self.window)
            
            pg.display.flip()


    def display_finish_message(self):
        font = pg.font.Font(FONTFILE,GAMEOVERFONTSIZE)
        surf = pg.Surface((WIDTH,HEIGHT),pg.SRCALPHA)
        x=0
        y=-GAMEOVERFONTSIZE
        for i in ["CONGRATS!","YOU SUCCESSFULLY","ESCAPED!"]:
            text = font.render(i,True,(255,255,255))
            rect = text.get_rect()
            rect.center = surf.get_rect().center
            rect.y+=y
            surf.blit(text,rect)
            y+= GAMEOVERFONTSIZE
        
        
        return surf
    

    def blitplayerart(self):
        self.screen.fill(1)
        art = pg.image.load(PLAYERART).convert_alpha()
        rect = art.get_rect()
        rect.y = HEIGHT//2 - rect.height
        self.screen.blit(art,rect)
        

    def display_credits(self):
        credits_running = True
        self.blitplayerart()
        font = pg.font.Font(FONTFILE,64)
        text = font.render("Credits",True,(255,255,255))
        rect = text.get_rect()
        rect.center =self.screen.get_rect().center
        rect.y = 0
        self.screen.blit(text,rect)
        credits = pg.sprite.Group()
        offset = 0
        for c in [["Font","Chris Vile"],["Art and Dev","Bhargav"],["Music","Google Song Maker"]]:
            credit = CreditText(c[0],self,offset)
            offset+=64
            credits.add(credit)
            credit = CreditText(c[1],self,offset)
            offset+=96+32
            credits.add(credit)

        while credits_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            
            self.display_window()
            credits.update()
            credits.draw(self.window)
            pg.display.flip()

    def finish_loop(self):
        self.load_music('music 1')
        self.finish_running = True
        self.blitplayerart()
        surf =self.display_finish_message()
        last_update = pg.time.get_ticks()
        thresh = 1700
        while self.finish_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            
            self.display_window()
            self.window.blit(surf,(0,-100))
            now = pg.time.get_ticks()
            if now - last_update > thresh:
                self.finish_running = False
                self.display_credits()
                last_update = now
            
            pg.display.flip()


game = Game()
game.menu_loop()
                
            
    