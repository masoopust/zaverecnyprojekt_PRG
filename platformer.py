import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()                                         #inicializace pygame

        #okno
        pygame.display.set_caption("Ninja game")                #jméno okna

        self.screen = pygame.display.set_mode((640, 480))         #souřadnice 0,0 jsou vlevo nahoře
        self.clock = pygame.time.Clock()

        #mrak
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0, 0, 0))                               # tato barva (0,0,0)(černá)  bude transparentní a zmizí tak pozadí mraku

        self.img_pos = [160, 260]                                           #souřadnice pozice mraku
        self.movement = [False, False]

        #kolize
        self.collision_area = pygame.Rect(50, 50, 300, 50)




    def run(self):
        while True:
            self.screen.fill((14, 219, 248))          #každý frame se mi změní na tuto barvu + to co se mi tam vyrenderuje

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(),self.img.get_height())  # vytvoří obdelník pro zobrazení kolizí
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)                        #když je mrak v kolizi s obbdelníkem svítí barva (0, 100, 255)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)                         #když mrak není v kolizi s obbdelníkem svítí barva (0, 50, 155)

            self.img_pos[1] += self.movement[1] * 5 - self.movement[0] * 5       # *5 zvyšuje rychlost pohybu
            self.screen.blit(self.img, self.img_pos)                        #vykreslení mraku na souřadnicích self.img_pos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                       #nekonečný cyklus mi kontroluje zmačknutí křížku, popřípadě quitne hru
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:                            #kontroluje zmáčknutí up klávesy
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:                          #kontroluje zmáčknutí down klávesy
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:                            #kontroluje puštění up klávesy
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:                          #kontroluje puštění down klávesy
                        self.movement[1] = False

            pygame.display.update()                     #update obrazovky
            self.clock.tick(60)                         #60FPS    SELF--> pointer na třídu

Game().run()






























