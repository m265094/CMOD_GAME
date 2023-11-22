import pygame
import sys
from game_parameters import *
mids_position = (10, 3)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/puffer_fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = MAX_SPEED
        self.rect.center = (x,y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y


    def draw_projectile(mid_pos):
        pygame.draw.rect(screen, BLUE, (mid_pos[0] * CELL_SIZE, mid_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def add_projectile(num_projectiles):
        for _ in range(num_projectiles):
            projectiles.add(Projectile(mids_position))

enemies = pygame.sprite.Group()