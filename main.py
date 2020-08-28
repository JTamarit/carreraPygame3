import pygame, sys
import random

class Runner():
    
    __customes =('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0, custome='turtle'):
        self.custome =pygame.image.load("images/{}.png".format(custome))
        self.position =[x, y]
        self.name = custome
    
    def avanzar(self):
        self.position[0] += random.randint(1,6)
        
        
    
    

class Game():
    
    runners=[]
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    __posY=(160,200,240,280)
    __startLine = -10
    __finishLine = 620 
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background=pygame.image.load("images/background.png")
        pygame.display.set_caption("CARRERA DE BICHOS")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
        
    def competir(self):
        gameOver=False
        
        while not gameOver:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    gameOVer = True
                    
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
                
            
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
    
    
    
if __name__=='__main__':
    
    game = Game()
    pygame.font.init()
    game.competir()
    