import pygame, sys

class Game():
    runners=[] 
    _starLine = 20
    _finishLine = 620 
    
    def __init__(self):
        self._screen = pygame.display.set_mode((640,480))
        self._background=pygame.image.load("images/background.png")
        pygame.dsiplay.ser_caption ("CARRERA DE BICHOS")
        
        
    
    
    
if __name__='__main__':
    game = Game()
    