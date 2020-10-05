# import pygame module in this program 
import pygame 
import random
import time 
import string
import pygame.freetype  # Import the freetype module.

def generateLine():
    matrix = ''
    for i in range (0, 10):
        n = random.choice(string.printable)
        matrix = matrix + n + ' '
    return matrix

pygame.init()
screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.SysFont('freesansbold.ttf', 32)
running =  True
i = 0

MAX_X = 10
MAX_Y = 10
SPACING = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    # You can use `render` and then blit the text surface ...
    # text_surface, rect = GAME_FONT.render("Hello World!", (0, 0, 0))
    # screen.blit(text_surface, (40, 250))
    # or just `render_to` the target surface.

    for j in range (1, MAX_Y):
        GAME_FONT.render_to(screen, (40, 40 + (SPACING * j)), generateLine(), (0, 0, 0))

    pygame.display.flip()
    time.sleep(1)

pygame.quit()