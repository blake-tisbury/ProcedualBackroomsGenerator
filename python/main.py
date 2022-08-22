from math import ceil
import pygame
import kruskal_generation

pygame.init()
pygame.display.set_caption('Procedural Backrooms Generator')

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode([screen_width, screen_height])

screen.fill((0, 0, 0))

vel = 5
scale = 2
wall_thickness = ceil(1 * scale)
hall_width = ceil(6 * scale)
run = True
kruskal_maze_generator = kruskal_generation.KruskalMaze(66)
maze = kruskal_maze_generator.generate_maze(.4)


def make_wall(x, y, edge):
    x_length = abs(edge[0][0] - edge[1][0]) * hall_width + wall_thickness
    y_length = abs(edge[0][1] - edge[1][1]) * hall_width + wall_thickness
    if x_length == 0:
        x_length = wall_thickness
    if y_length == 0:
        y_length = wall_thickness

    x_local = x + (edge[0][0] * hall_width + wall_thickness)
    y_local = y + (edge[0][1] * hall_width + wall_thickness)

    pygame.draw.rect(screen, [255, 255, 255], [x_local, y_local, x_length, y_length])


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(maze) > 0:
        make_wall(0, 0, maze.pop())

    # delay
    pygame.time.delay(1)
    pygame.display.update()

pygame.quit()
