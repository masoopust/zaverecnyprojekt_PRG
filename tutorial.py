# věci pomoci kterých jsem pochopil backend hry




# Naučení principu kolize
"""
# mrak
self.img = pygame.image.load("data/images/clouds/cloud_1.png")
self.img.set_colorkey((0, 0, 0))                                         # tato barva (0,0,0)(černá)  bude transparentní a zmizí tak pozadí mraku

self.img_pos = [160, 260]                                                    # souřadnice pozice mraku
self.movement = [False, False]

# kolize
self.collision_area = pygame.Rect(50, 50, 300, 50)


img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(),self.img.get_height())        # vytvoří obdelník pro zobrazení kolizí
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)                        #když je mrak v kolizi s obbdelníkem svítí barva (0, 100, 255)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)                         #když mrak není v kolizi s obbdelníkem svítí barva (0, 50, 155)

            self.img_pos[1] += self.movement[1] * 5 - self.movement[0] * 5                               # *5 zvyšuje rychlost pohybu
            self.screen.blit(self.img, self.img_pos)                                                     #vykreslení mraku na souřadnicích self.img_pos
"""








