import pygame
pygame.init()

WIDTH, HEIGHT = 300, 500
FPS = 35
CELL = 20
ROWS = (HEIGHT - 120) // CELL
COLS = WIDTH // CELL


BLACK = (0,0,0)
WHITE = (255, 255, 255)
BG_COLOR = (31, 25, 76)
GRID = (31, 25, 132)
WIN = (50, 230, 50)
LOSE = (252, 91, 122)

font = pygame.font.SysFont("verdana",50)
font2  = pygame.font.SysFont("verdana", 15)

ASSETS ={
    1: pygame.image.load("Assets/1.png"),
    2: pygame.image.load("Assets/2.png"),
    3: pygame.image.load("Assets/3.png"),
    4: pygame.image.load("Assets/4.png")
}