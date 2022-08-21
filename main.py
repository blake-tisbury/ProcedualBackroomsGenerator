import random
import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode([screen_width, screen_height])

vel = 5
wall_size = 10
run = True


def make_wall(x, y, filled):
    pygame.draw.rect(screen, [255, 255, 255] if filled else [40,40,40], [x, y, wall_size, wall_size])


def make_zone(zone_size):
    zone_size = zone_size * wall_size

    x = int(screen_width / 2 - (zone_size / 2))
    y = int(screen_height / 2 - (zone_size / 2))

    # makes a grid of square tiles
    for i in range(x, x + zone_size, wall_size):
        for j in range(y, y + zone_size, wall_size):
            make_wall(i, j, (random.choices(population=[True, False], weights=[0.3, 0.7], k=1)[0]))


screen.fill((0, 0, 0))

make_zone(100)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()

    pygame.display.update()

pygame.quit()




