import pygame
import sys
from game_parameters import *

#mid_possible_positions = {
 #   1:(4,3)
 #   2:(10, 3)
 #   3:(16, 3)
 #   4:(4,11)
 #   5:(10, 11)
 #   6:(16, 11)
#}



def draw_mid(mid_pos):
        pygame.draw.rect(screen, GREEN, (mid_pos[0] * CELL_SIZE, mid_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#def pick_random
    #randomint in range(1,6)

#def draw_mid(randomint in range(mid_possible_positions)):
  #  pygame.draw.rect(screen, RED, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
