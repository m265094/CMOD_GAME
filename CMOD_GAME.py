import pygame
import sys
from game_parameters import *
from maze import draw_maze
from maze import draw_maze_2
from CMOD import draw_player
from CMOD import move_player
from mids import draw_mid
from projectile import *
# Initialize Pygame
pygame.init()

lives = NUM_LIVES
score = 0
score_font = pygame.font.Font("../CMOD_game/assets/fonts/Branda-yolq.ttf", 80)

# Initial player position
player_position = (4, 3)
mids_position = (10, 3)

#g
# Main game loop
running = True
while lives > 0 and running:
    for event in pygame.event.get():
        #print(event)
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

    #Projectile.update()

    #draw the score on the screen
    text = score_font.render(f"Wave #{score}", True, (255, 0, 0))
    screen.blit(text, (WIDTH - CELL_SIZE*8.5, 0))

    #for i in range(lives):
    #    screen.blit(life_icon, (i*CELL_SIZE, MAZE_HEIGHT - CELL_SIZE))
    # show game over message
    message = score_font.render("GAME OVER!!!", True, (255, 0, 0))
    screen.blit(message, (WIDTH / 2 - message.get_width() / 2, HEIGHT / 2 - message.get_height() / 2))
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text,
                (WIDTH / 2 - score_text.get_width() / 2, HEIGHT / 2 - 3 * score_text.get_height() / 2))

    pygame.display.flip()

    clock.tick(60)

    screen.fill(WHITE)
    draw_maze()
    draw_player(player_position)
    draw_mid(mids_position)


    pygame.display.flip()
    clock.tick(FPS)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

pygame.quit()
sys.exit()