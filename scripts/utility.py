import pygame

BASE_IMG_PATH = "data/images/"       #zkratka abych nemusel vypisovat pokaždé celou cestu


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))      # černá se stane transparentní
    return img














