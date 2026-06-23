import pygame
import sys

pygame.init()
pygame.display.set_caption("McKinley")
screen = pygame.display.set_mode((600, 400))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(pygame.Color("Gray"))
    pygame.draw.circle(screen, pygame.Color("Blue"), (screen.get_width() / 2, screen.get_height() / 2), 100)

    pygame.display.update()
