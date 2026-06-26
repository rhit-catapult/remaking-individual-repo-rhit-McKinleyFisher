import pygame
import random  
import raindrop_module


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
       self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        drop_x = random.randint(self.x + 10, self.x + self.image.get_width() - 10)
        drop_y = self.y + self.image.get_height() - 5
        new_raindrop = raindrop_module.Raindrop(self.screen, drop_x, drop_y)
        self.raindrops.append(new_raindrop)

