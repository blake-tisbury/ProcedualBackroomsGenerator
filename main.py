import random
import pygame

from kruskal_generation import random_kruskal_maze

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode([screen_width, screen_height])

vel = 5
wall_thickness = 2
scale = 20
run = True


def make_wall(edge, filled):
    x_length = abs(edge[0][0] - edge[1][0]) * scale
    y_length = abs(edge[0][1] - edge[1][1]) * scale
    if x_length == 0:
        x_length = wall_thickness
    if y_length == 0:
        y_length = wall_thickness

    x = edge[0][0] * scale + wall_thickness
    y = edge[0][1] * scale + wall_thickness

    pygame.draw.rect(screen, [255, 255, 255] if filled else [40, 40, 40], [x, y, x_length, y_length])


def make_zone(zone_size):
    zone_size = zone_size * wall_thickness

    x = int(screen_width / 2 - (zone_size / 2))
    y = int(screen_height / 2 - (zone_size / 2))

    # makes a grid of square tiles
    for i in range(x, x + zone_size, wall_thickness):
        for j in range(y, y + zone_size, wall_thickness):
            make_wall(i, j, (random.choices(population=[True, False], weights=[0.3, 0.7], k=1)[0]))


screen.fill((0, 0, 0))

# make_zone(100)

maze = random_kruskal_maze(100)
index = 0

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()

    if index < len(maze):
        make_wall(maze[index], True)
        index += 1

    # delay
    pygame.time.delay(1)
    pygame.display.update()

pygame.quit()
