from settings import *
from player import Player
from leveleditor import Level




class Game:
    def __init__(self):
        self.screen = pg.Surface((WIDTH//2,HEIGHT//2))

        
        self.fog = pg.Surface((WIDTH,HEIGHT),pg.SRCALPHA)
        self.debug = False
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.new_level()
        self.fade_out = True
        self.has_key = False
    

    def new_level(self,lvl=1,cords=None):
        
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.camera = pg.sprite.Group()

        self.level = Level(lvl)
        for collec in self.level.collectibles:
            self.all_sprites.add(collec)

        cords = self.level.playercords if not cords else cords
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
        

        
        

        
            

    def run(self):
        

        while True:
            self.dt = self.clock.tick(FPS)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            
            self.player_sprite.update()
            self.draw_screen()
            self.display_window()
            pg.display.update()
    



game = Game()
game.run()
                
            
    