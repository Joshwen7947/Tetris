import pygame
import random 
import sys
from variables import *
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

class Shape:
    VERSION = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }
    SHAPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']
    
    # Constructor
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.type = random.choice(self.SHAPES)
        self.shape = self.VERSION[self.type]
        self.color = random.randint(1,4)
        self.orientation = 0
    
    # image ~ Version of the Shape
    def image(self):
        return self.shape[self.orientation] 
    
    # rotate
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.shape)
    

# Game Class
class Tetris:
    # Constructor 
    def __init__(self, rows, cols):
        self.rows = rows 
        self.cols = cols
        self.score = 0
        self.level = 1
        self.grid = [[0 for j in range(cols)] for i in range(rows)]
        self.next = None
        self.end = False
        self.new_shape()
        
    # Make Grid
    def make_grid(self):
        for i in range(self.rows+1):
            pygame.draw.line(SCREEN, GRID, (0,CELL*i), (WIDTH,CELL*i))
        for j in range(self.cols+1):
            pygame.draw.line(SCREEN, GRID, (CELL*j, 0),(CELL*j, HEIGHT-120))
    
    # Make new shape
    def new_shape(self):
        if not self.next:
            self.next = Shape(5,0)
        self.figure = self.next
        self.next = Shape(5,0)
        
    # COLLISION
    def collision(self) -> bool:
        for i in range(4):
            for j in range(4):
                if (i*4 +j) in self.figure.image():
                    block_row = i + self.figure.y
                    block_col = j + self.figure.x
                    if (block_row >= self.rows or block_col >= self.cols or block_col < 0 or self.grid[block_row][block_col] > 0):
                        return True
        return False
        
    # Remove Row
    def remove_row(self):
        rerun = False
        
        for y in range(self.rows-1, 0, -1):
            completed = True
            for x in range(0, self.cols):
                if self.grid[y][x] == 0:
                    completed = False
        
            if completed:
                del self.grid[y]
                self.grid.insert(0, [0 for i in range(self.cols)])
                self.score += 1
                if self.score % 10 == 0:
                    self.level += 1
                rerun = True
        
        if rerun:
            self.remove_row()
  
    # Freeze 
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if (i*4+j) in self.figure.image():
                    self.grid[i+self.figure.y][j+self.figure.x] = self.figure.color
          
        self.remove_row()          
        self.new_shape()
        if self.collision():
            self.end = True
                 
    # Move Down
    def move_down(self):
        self.figure.y += 1
        if self.collision():
            self.figure.y -= 1
            self.freeze()
    
    # Move Left
    def left(self):
        self.figure.x -= 1
        if self.collision():
            self.figure.x += 1
    
    # Move Right
    def right(self):
        self.figure.x += 1
        if self.collision():
            self.figure.x -= 1
    
    # freefall
    def freefall(self):
        while not self.collision():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()
    
    # Rotate
    def rotate(self):
        orientation = self.figure.orientation
        self.figure.rotate()
        if self.collision():
            self.figure.orientation = orientation
        
    def end_game(self):
        popup = pygame.Rect(50,140,WIDTH-100, HEIGHT - 350)
        pygame.draw.rect(SCREEN, BLACK, popup)
        pygame.draw.rect(SCREEN, LOSE, popup, 2)
        
        game_over = font2.render("GAME OVER!", True, WHITE)
        option1 = font2.render("Press r to restart", True, LOSE)
        option2 = font2.render("Press q to quit", True, LOSE)
        
        SCREEN.blit(game_over, (popup.centerx-game_over.get_width()/2, popup.y + 20))
        SCREEN.blit(option1, (popup.centerx-option1.get_width()/2, popup.y + 80))
        SCREEN.blit(option2, (popup.centerx-option2.get_width()/2, popup.y + 110))
    