from settings import *
from player import Player
from leveleditor import Level




class Game:
    def __init__(self):
        self.screen = pg.Surface((WIDTH//2,HEIGHT//2))
        self.all_sprites = pg.sprite.Group()
        self.camera = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.bg = pg.image.load(BGIMAGE).convert_alpha()
        self.fog = pg.Surface((WIDTH,HEIGHT),pg.SRCALPHA)
        self.debug = False
        self.level = Level(1)
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
        


    def display_window(self):
        
        self.window.fill(1)
        
        if self.debug:
            pg.draw.rect(self.screen,(0,255,0),self.player.rect,width=2)
            for wall in self.level.walls:
                pg.draw.rect(self.screen,(255,0,0),wall.rect,width=2)

        surf = pg.transform.scale(self.screen,(WIDTH,HEIGHT))
        self.window.blit(surf,(0,0))
        #Draw walls
        
        
            
            


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()


            self.screen.fill(1)
            self.screen.blit(self.bg,(0,0))
            if not self.debug:
                self.fog.fill(FOG_COLOR)
                self.camera.draw(self.fog)
                self.screen.blit(self.fog,(0,0),special_flags=pg.BLEND_MULT)
            else:
                self.camera.draw(self.screen)
            
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            self.display_window()
            pg.display.update()
    



game = Game()
game.run()
                
            
    