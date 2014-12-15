import pygame
from pygame.locals import *
from gamelib import SimpleGame
from Zumo import Zumo
from Elements import GameProp

class ZumoGame(SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GAME_WIDTH = 800
    ZumoSize_WIDTH = 137
    is_Win = False
    is_Started = False 
 
 
    def __init__(self):
        super(ZumoGame, self).__init__('Zumo', ZumoGame.BLACK)
 
    def init (self):
        super(ZumoGame, self).init()
        self.init_Bg()
        self.init_Zumo()
                
    def init_Bg (self):
        self.bg = pygame.image.load("ZumoRing.png")
        
        
    def init_Zumo(self):
       
        self.Zumo1 = Zumo("Sumo_Player1.png",ZumoGame.GAME_WIDTH/2-ZumoGame.ZumoSize_WIDTH,200)
        self.Zumo2 = Zumo("Sumo_Player2.png",ZumoGame.GAME_WIDTH/2,200)
    
    def init_Prop():
        self.Number1 = Elements(self,"NumberOne.png",ZumoGame.GAME_WIDTH/2,ZumoGame.GAME_HEIGHT/3)
        self.Number2 = Elements(self,"NumberTwo.png",ZumoGame.GAME_WIDTH/2,ZumoGame.GAME_HEIGHT/3)
        self.Number3 = Elements(self,"NumberThree.png",ZumoGame.GAME_WIDTH/2,ZumoGame.GAME_HEIGHT/3)
        self.Number3 = Elements(self,"Fight.png",ZumoGame.GAME_WIDTH/2,ZumoGame.GAME_HEIGHT/3)

    def update(self):
        self.Zumo1.update()
        self.Zumo2.update()
        self.CheckWin()
        
        if(not ZumoGame.is_Win):
            if self.is_key_pressed(K_q) or self.is_key_pressed(K_z):
                self.Zumo1_Push()
                self.Zumo1.count += 1
                print("count1 ")
                print(self.Zumo1.count)
            if self.is_key_pressed(K_o) or self.is_key_pressed(K_m): 
                self.Zumo2_Push()
                self.Zumo2.count += 1
                print("count2 ")
                print(self.Zumo2.count)
            elif ( self.is_key_pressed(K_q) or self.is_key_pressed(K_z) ) and ( self.is_key_pressed(K_o) or self.is_key_pressed(K_m) ):
                self.Zumo1.count += 0
                self.Zumo2.count += 0
                
        if self.is_key_pressed(K_SPACE):
            self.restart()
        
 
    def render(self, surface):
        self.surface.blit(self.bg,(0,0))
        self.Zumo1.render(surface)
        self.Zumo2.render(surface)
        
    def Zumo1_Push(self):
        self.Zumo1.posX += 2
        self.Zumo2.posX += 2
       
    def Zumo2_Push(self):
         self.Zumo2.posX -= 2 
         self.Zumo1.posX -= 2
    
    
    def CheckWin(self):
        if self.Zumo1.count >= 200 :
            self.Zumo2.posX += 10
            ZumoGame.is_Win = True
        if self.Zumo2.count >= 200 :
            self.Zumo1.posX -= 10
            ZumoGame.is_Win = True
        
    def StartGame(self):
        pass 
           
      
    def restart(self):
        self.Zumo1.posX = ZumoGame.GAME_WIDTH/2-ZumoGame.ZumoSize_WIDTH
        self.Zumo2.posX = ZumoGame.GAME_WIDTH/2
        self.Zumo1.count = 0
        self.Zumo2.count = 0
        ZumoGame.is_Win = False
        self.StartGame()
    # ...
    
def main():
    game = ZumoGame()
    game.run()
 
if __name__ == '__main__':
    main()
