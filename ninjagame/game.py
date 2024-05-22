import sys
import pygame

from scripts.entities import PhysicsEntity      #ze složky scripts, souboru entities, importne třídu Physics entities
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:
    def __init__(self):
        pygame.init()                                         #inicializace pygame

        #okno
        pygame.display.set_caption("Ninja game")                  #jméno okna
        self.screen = pygame.display.set_mode((640, 480))         #souřadnice 0,0 jsou vlevo nahoře

        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "decor": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "large_decor": load_images("tiles/large_decor"),
            "stone": load_images("tiles/stone"),
            "player": load_image("entities/player.png"),
            "background": load_image("background.png"),
            "clouds": load_images("clouds"),
        }

        self.clouds = Clouds(self.assets["clouds"], count = 16)

        #hráč
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))     #spawne panáčka na pozici 50,50 o velikosti 8x15

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.blit(self.assets["background"], (0, 0))          #přidá se pozadí

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30           # kamera se mi pohybuje s panáčkem (centruje ho na střed)
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))                                                    # kamera se bude pohybovat po celých číslech (int), nemůžu  řešit desetinná čísla

            self.clouds.update()
            self.clouds.render(self.display, offset = render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))         # na ose Y je 0 protože platformer je zleva doprava a naopak
            self.player.render(self.display, offset = render_scroll)

            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                                           #nekonečný cyklus mi kontroluje zmačknutí křížku, popřípadě quitne hru
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:                            #kontroluje zmáčknutí left klávesy
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:                          #kontroluje zmáčknutí right klávesy
                        self.movement[1] = True
                    if event.key == pygame.K_UP:                               #kontroluje zmáčknuti šipky nahoru
                        self.player.velocity[1] = -3                           #skočí o 3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:                            #kontroluje puštění left klávesy
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:                          #kontroluje puštění right klávesy
                        self.movement[1] = False


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()                                          #update obrazovky
            self.clock.tick(60)                                              #60FPS    SELF--> pointer na třídu



Game().run()






























