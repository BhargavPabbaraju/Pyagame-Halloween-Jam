from settings import *
from player import Player




pg.init()
clock = pg.time.Clock()

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.all_sprites = pg.sprite.Group()
        self.camera = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.bg = pg.image.load(BGIMAGE).convert_alpha()
        self.fog = pg.Surface((WIDTH,HEIGHT))
        self.fog.fill(FOG_COLOR)




    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()


            self.screen.fill(1)
            self.fog.fill(FOG_COLOR)
            self.screen.blit(self.bg,(0,0))
            self.camera.draw(self.fog)
            self.screen.blit(self.fog,(0,0),special_flags=pg.BLEND_MULT)
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            pg.display.update()
    



game = Game()
game.run()
                
            
    