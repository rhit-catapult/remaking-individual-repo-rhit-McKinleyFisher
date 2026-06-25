import pygame
import sys
import time  
import random  


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 10)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > self.screen.get_height()

    def draw(self):
        pygame.draw.line(self.screen, pygame.Color("Dark Blue"), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen: pygame.Surface, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        if time.time() > self.last_hit_time + 0.5:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        hit_box = pygame.Rect(self.x, self.y, self.image_umbrella.get_width(), self.image_umbrella.get_height())
        return hit_box.collidepoint(raindrop.x, raindrop.y)


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
        drop_x = random.randint(self.x + 3, self.x + self.image.get_width() - 3)
        drop_y = self.y + self.image.get_height() - 5
        new_raindrop = Raindrop(self.screen, drop_x, drop_y)
        self.raindrops.append(new_raindrop)


def main():
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    mike = Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = Cloud(screen, 300, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        cloud_speed = 10
        if pressed_keys[pygame.K_UP]:
            cloud.y -= cloud_speed
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += cloud_speed
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += cloud_speed
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= cloud_speed

        screen.fill((255, 255, 255))
        cloud.draw()
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        alyssa.draw()
        pygame.display.update()
    
main()
