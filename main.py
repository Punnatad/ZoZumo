import pygame
from pygame.locals import *

import pygame
from pygame.locals import *

import gamelib
from gamelib import SimpleGame

from elements import Zumo

  

class ZumoPlace(SimpleGame):  
    BLACK = pygame.Color('black')
        
    def __init__(self):
        super(ZumoPlace, self).__init__('Zumo', ZumoPlace.BLACK)
     

    def init(self):
        super(ZumoPlace, self).init()
        #self.render_score()
        self.Zumo1_Hit = 0
        self.Zumo2_Hit = 0
        self.init_Bg()
        #self.init_Zumo()
        
        
                          
    def init_Bg(self):
        self.bg = pygame.image.load("ZumoRing.png")
        self.surface.blit(self.bg,(0,0))
          
        
   ## def init_Zumo(self):
     ##   self.Zumo1 = Zumo("Zumo_Player1.png",300 ,100)
       ## self.Zumo2 = Zumo("Zimo_Plyaer2.png",600 ,100)


    def update(self):
        print"SS"
        self.surface.blit(self.bg,(0,0))
       ## self.Zumo1.update()
       ## self.Zumo2.update()
        self.CheckHit()
     
    def render(self,surface):
        ##self.Zumo1.render(surface)
        ##self.Zumo2.render(surface)
       
        pass
    def CheckHit(self):
        pass
       
def main():
    game = ZumoPlace()
    game.run()

if __name__ == '__main__':
    main()
