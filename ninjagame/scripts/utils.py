import os

import pygame

BASE_IMG_PATH = "data/images/"       #zkratka abych nemusel vypisovat pokaždé celou cestu


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))      # černá se stane transparentní
    return img


def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):   # os.listdir vezme cestu o vezme všechny soubory co jsou na té cestě
        images.append(load_image(path + "/" + img_name))
        return images











