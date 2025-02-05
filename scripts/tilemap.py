import pygame

TOUCHING = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}
TILEs_ID = {'0': None, '1': 'stone'}


class Tilemap:
    def __init__(self, game, map, tile_size=64,):
        self.game = game
        self.map = map
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(len(map)):
            for j in range(len(map[i])):
                if TILEs_ID[map[i][j]]:
                    self.tilemap[str(j) + f';{str(i)}'] = {'type': TILEs_ID[map[i][j]], 'variant': 1, 'pos': (j, i)}

    def tile_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for pair in TOUCHING:
            check_loc = str(tile_loc[0] + pair[0]) + ';' + str(tile_loc[1] + pair[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tile_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(
                    pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size,
                                self.tile_size))
        return rects

    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']],
                      (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))