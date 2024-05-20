import sys
import pygame

from scripts.entities import PhysicsEntity      #ze složky scripts, souboru entities, importne třídu Physics entities
from scripts.utility import load_image

class Game:
    def __init__(self):
        pygame.init()                                         #inicializace pygame

        #okno
        pygame.display.set_caption("Ninja game")                #jméno okna
        self.screen = pygame.display.set_mode((640, 480))         #souřadnice 0,0 jsou vlevo nahoře

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "Player": load_image("entities/player.png")
        }

        #hráč
        self.player = PhysicsEntity(self, "player", (50,50), (8,15))     #spawne panáčka na pozici 50,50 o velikosti 8x15



    def run(self):
        while True:
            self.screen.fill((14, 219, 248))          #každý frame se mi změní na tuto barvu + to co se mi tam vyrenderuje

            self.player.update((self.movement[1] - self.movement[0], 0))         # na ose Y je 0 protože platformer je zleva doprava a naopak

            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                                           #nekonečný cyklus mi kontroluje zmačknutí křížku, popřípadě quitne hru
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:                            #kontroluje zmáčknutí rleft klávesy
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:                          #kontroluje zmáčknutí right klávesy
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:                            #kontroluje puštění left klávesy
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:                          #kontroluje puštění right klávesy
                        self.movement[1] = False

            pygame.display.update()                                          #update obrazovky
            self.clock.tick(60)                                              #60FPS    SELF--> pointer na třídu



Game().run()






























