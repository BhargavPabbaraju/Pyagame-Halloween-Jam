from settings import *

class Game:
    def __init__(self):
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
    



    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()


            self.window.fill(-1)
            pg.display.update()
    



game = Game()
game.run()
                
            
    