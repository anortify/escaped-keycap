import sys

import pygame

from scripts.utils import load_image, load_images, load_lvl
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        self.JumpHeight = 22

        pygame.display.set_caption('escaped keycap')
        self.screen = pygame.display.set_mode((1600, 900))
        self.display = pygame.Surface((1600, 900))
        self.lvl = load_lvl("lvl1.txt")

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'map': load_lvl("lvl1.txt"),
            'background': load_images('background'),
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (100, 600), (57, 62))

        self.tilemap = Tilemap(self, self.assets["map"], tile_size=64)

    def run(self):
        is_facing_right = True
        while True:
            self.display.blit(self.assets['background'][0], (0, 0))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, is_facing_right)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        is_facing_right = False
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        is_facing_right = True
                        self.movement[1] = True
                    if event.key == pygame.K_UP and self.player.ON_GROUND:
                        self.player.velocity[1] = self.JumpHeight * -1
                        self.player.ON_GROUND = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()