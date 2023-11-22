import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CELL_SIZE = 40
MAZE_WIDTH = WIDTH // CELL_SIZE
MAZE_HEIGHT = HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create Maze
row_0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
row_1 = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0]
row_2 = [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]

maze = [row_0, row_0, row_1, row_1, row_1, row_1, row_2, row_2, row_2, row_1, row_1, row_1, row_1, row_0, row_0]

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

def draw_maze():
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            if maze[row][col] == 1:
                color = WHITE
            else:
                color = BLACK
            #color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player(player_pos):
    pygame.draw.rect(screen, RED, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_player(player_pos, direction):
    new_pos = player_pos
    print(player_pos)
    if direction == "UP" and player_pos[1] > 0 and maze[player_pos[1] - 1][player_pos[0]] == 1:
        new_pos = (player_pos[0], player_pos[1] - 1)
    elif direction == "DOWN" and player_pos[1] < MAZE_HEIGHT - 1 and maze[player_pos[1] + 1][player_pos[0]] == 1:
        new_pos = (player_pos[0], player_pos[1] + 1)
    elif direction == "LEFT" and player_pos[0] > 0 and maze[player_pos[1]][player_pos[0] - 1] == 1:
        new_pos = (player_pos[0] - 1, player_pos[1])
    elif direction == "RIGHT" and player_pos[0] < MAZE_WIDTH - 1 and maze[player_pos[1]][player_pos[0] + 1] == 1:
        new_pos = (player_pos[0] + 1, player_pos[1])

    return new_pos

# Initial player position
player_position = (3, 3)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_position = move_player(player_position, "UP")
            elif event.key == pygame.K_DOWN:
                player_position = move_player(player_position, "DOWN")
            elif event.key == pygame.K_LEFT:
                player_position = move_player(player_position, "LEFT")
            elif event.key == pygame.K_RIGHT:
                player_position = move_player(player_position, "RIGHT")

    screen.fill(WHITE)
    draw_maze()
    draw_player(player_position)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()