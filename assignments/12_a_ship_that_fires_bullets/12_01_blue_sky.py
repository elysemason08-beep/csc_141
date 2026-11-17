#Ciani Mason
# lowkey confuesd thought i did this one already but ok.
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Blue Sky")

bg_color = (135, 206, 250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg_color)
    pygame.display.flip()