import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}  # všechny tiles
        self.offgrid_tiles = []  # všechny tiles mimo grid

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    def tiles_around(self, pos):  # tato funkce načíta hodnoty kolem ninjy pro kontrolu kolize
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))  # // je dělení beze zbytku (zahodí ho)
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):  # projde všechny tiles v tiles_around podle pozice hráče
            if tile['type'] in PHYSICS_TILES:  # a když je tile v Physics tiles (je tráva nebo kámen)
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects  # přidají se do listu obdelník všchny obdelníky kde tiles sousedí s trávou nebo kamenem

    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))  # offset odečítám, protože kamera se pohne doprava tak vše na screenu se pohne doleva

        for x in range(offset[0] // self.tile_size,
                       (offset[0] + surf.get_width()) // self.tile_size + 1):  # chceme renderovat pouze pixely co jsou  na obrazovce podle pozice kamery, kterou zde zjišťujeme pomocí offset[0] // self.tile_size --> tím zjistíme levý horní pixel
            for y in range(offset[1] // self.tile_size, (offset[1] + surf.get_height()) // self.tile_size + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))


