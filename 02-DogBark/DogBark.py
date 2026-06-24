import pygame
import sys


def main():
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    pygame.init()
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    dogs_image = pygame.image.load("2dogs.JPG")
    dogs_image = pygame.transform.scale(dogs_image, (IMAGE_SIZE, IMAGE_SIZE))

    bottom_font = pygame.font.SysFont("Georgia", 28)
    bottom_caption = bottom_font.render("Two Dogs", True, BLACK)
    bark_sound = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        screen.fill(WHITE)
        screen.blit(dogs_image, (0,0))
        screen.blit(bottom_caption, (screen.get_width() / 2 - bottom_caption.get_width() / 2, screen.get_height() - bottom_caption.get_height() - 2))

        pygame.display.update()


main()
