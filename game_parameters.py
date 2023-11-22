import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CELL_SIZE = 40
MAZE_WIDTH = WIDTH // CELL_SIZE
MAZE_HEIGHT = HEIGHT // CELL_SIZE

# Colors
WHITE = (222, 212, 144)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)

# Create Maze
row_0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
row_1 = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0]
row_2 = [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
row_3 = [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,]


maze = [row_0, row_0, row_1, row_1, row_1, row_1, row_2, row_2, row_2, row_1, row_1, row_1, row_1, row_0, row_0]
maze_2 = [row_0, row_2, row_2, row_2, row_3, row_3, row_2, row_2, row_2, row_3, row_3, row_2, row_2, row_2, row_0]

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

#Set number of lives
NUM_LIVES = 3