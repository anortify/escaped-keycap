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


def load_lvl(path):
    lvl_map = []
    with open((BASE_LVL_MAPS_PATH + path), "r") as f:
        lvl_map = [list(i.rstrip('\n')) for i in f.readlines()]
    return lvl_map