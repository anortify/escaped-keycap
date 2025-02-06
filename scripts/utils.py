import os

import pygame


BASE_IMG_PATH = 'data/images/'
BASE_LVL_MAPS_PATH = 'data/maps/'


def load_image(path):

    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images


def load_lvls():
    lvl_maps = []
    for map in sorted(os.listdir(BASE_LVL_MAPS_PATH)):
        with open((BASE_LVL_MAPS_PATH + map), "r") as f:
            g = f.readlines()
            lvl_maps.append({"playerPos": g[-1], "map": [list(i.rstrip('\n')) for i in g[:-2]]})
    print(lvl_maps)
    return lvl_maps