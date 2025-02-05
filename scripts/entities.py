import pygame


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.ON_GROUND = False
        self.CoyoteTime = 0
        self.size = size
        self.velocity = [0, 0]
        self.MaxGravity = 18
        self.Gravity = 0.8
        self.SpeedMult = 7
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frame_movement = ((movement[0] + self.velocity[0]) * self.SpeedMult, movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = self.ON_GROUND = True
                    self.CoyoteTime, self.velocity[1] = 2, self.MaxGravity
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(self.MaxGravity, self.velocity[1] + self.Gravity)
        self.CoyoteTime -= 0.2

        if self.collisions['up']:
            self.velocity[1] = 0

        if not self.collisions['down'] and self.ON_GROUND:
            if self.velocity[1] == self.MaxGravity:
                self.pos[1] -= frame_movement[1]
                self.velocity[1] = 0
            if self.CoyoteTime <= 0:
                self.ON_GROUND = False

    def render(self, surf, flag):
        if flag:
            surf.blit(self.game.assets['player'], self.pos)
        else:
            surf.blit(pygame.transform.flip(self.game.assets["player"], True, False), self.pos)
