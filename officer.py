import pygame
import sys
from game_parameters import *
#clock object
clock = pygame.time.Clock()

def draw_officer(officer_pos):
    #create officer sprite randomly in the second range of 100 to 150
    if random.randint(1,9) < 7:
        clock.tick(60)
        officer_pos = (16,16)
        pygame.draw.rect(screen, BLUE, (officer_pos[0] * CELL_SIZE, officer_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
