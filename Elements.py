import pygame
from pygame.locals import *

class GameProp(object):

    def __init__(self,Path,posX,posY):
        self.posX = posX
        self.posY = posY
        self.GameProp = pygame.image.load(Path)
        
    def update(self):
        pass
       
    def render(self, surface):
        surface.blit(self.Zumo,(self.posX,self.posY))