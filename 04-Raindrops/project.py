import pygame
import sys
import time  
import hero_module
import cloud_module


def main():
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = cloud_module.Cloud(screen, 300, 50, "cloud.png")

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
