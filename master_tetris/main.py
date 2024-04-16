# Tetris in PyGame
import pygame
import random
import sys
from variables import *
from classes import Shape, Tetris

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

# Main Game Loop
def main():
    tetris = Tetris(ROWS, COLS)
    clock = pygame.time.Clock()
    counter = 0
    move = True
    space_pressed = False
    run = True
    while run:
        SCREEN.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            # Event Loop
        
            keys = pygame.key.get_pressed()
            if not tetris.end:
                if keys[pygame.K_LEFT]:
                    tetris.left()
                elif keys[pygame.K_RIGHT]:
                    tetris.right()
                elif keys[pygame.K_DOWN]:
                    tetris.move_down()
                elif keys[pygame.K_UP]:
                    tetris.rotate()
                elif keys[pygame.K_SPACE]:
                    space_pressed = True
            if keys[pygame.K_r]:
                tetris.__init__(ROWS, COLS)
            if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                run = False 
                
        # Allows block to fall at constant rate
        counter += 1
        if counter >= 15000:
            counter = 0
                
        if move:
            if counter % (FPS //(tetris.level*2)) == 0:
                if not tetris.end:
                    if space_pressed:
                        tetris.freefall()
                        space_pressed = False
                    else:
                        tetris.move_down()
        
        tetris.make_grid()
        
        # Keep Fallen Shapes on Screen
        for x in range(ROWS):
            for y in range(COLS):
                if tetris.grid[x][y] > 0:
                    value = tetris.grid[x][y]
                    image = ASSETS[value]
                    SCREEN.blit(image, (y*CELL, x*CELL))
                    pygame.draw.rect(SCREEN, WHITE, (y*CELL, x*CELL, CELL, CELL), 1)
                    
        # Show Shape on Game Screen
        if tetris.figure:
            for i in range(4):
                for j in range(4):
                    if (i *4 + j) in tetris.figure.image():
                        shape = ASSETS[tetris.figure.color]
                        x = CELL * (tetris.figure.x + j)
                        y = CELL * (tetris.figure.y + i)
                        SCREEN.blit(shape, (x,y))
                        pygame.draw.rect(SCREEN, WHITE, (x,y,CELL,CELL),1)
                        
        # Control Panel
        if tetris.next:
            for i in range(4):
                for j in range(4):
                    if (i *4 + j) in tetris.next.image():
                        image = ASSETS[tetris.next.color]
                        x = CELL * (tetris.next.x + j -4)
                        y = HEIGHT -100 + CELL * (tetris.next.y +i)
                        SCREEN.blit(image,(x,y))
              
        if tetris.end:
            tetris.end_game()
        
        score_text = font.render(f"{tetris.score}",True, WHITE)
        level_text = font2.render(f"level: {tetris.level}",True, WHITE)
        SCREEN.blit(score_text,(250-score_text.get_width()//2, HEIGHT-110))
        SCREEN.blit(level_text,(250-level_text.get_width()//2, HEIGHT-30))
        
        pygame.display.update()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()        
