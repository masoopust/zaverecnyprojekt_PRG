import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()                                         #inicializace pygame
        pygame.display.set_caption("Ninja game")              #jméno okna
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                       #nekonečný cyklus mi kontroluje zmačknutí křížku, popřípadě quitne
                    sys.exit()
            pygame.display.update()                     #update obrazovky
            self.clock.tick(60)                         #60FPS  SELF--> pointer na třídu

Game().run()






























