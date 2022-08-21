from math import sqrt
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


# below this is an implementation of kruskal's algorithm that I found on GitHub, I might use some of this for generation
'''
## Kruskal's Algorithm for Maze Generation
## Neil Thistlethwaite

from PIL import Image
import random
import numpy as np

global GRAPH_SIZE, CELL_THICKNESS, WALL_THICKNESS

## Maze generation parameters. Change as desired.
GRAPH_SIZE = 30
CELL_THICKNESS = 20
WALL_THICKNESS = 5

nodes = [(i, j) for j in range(GRAPH_SIZE) for i in range(GRAPH_SIZE)]
neighbors = lambda n: [(n[0] + dx, n[1] + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
                       if n[0] + dx >= 0 and n[0] + dx < GRAPH_SIZE and n[1] + dy >= 0 and n[1] + dy < GRAPH_SIZE]


## Somewhat naive implementation, as it doesn't do rank balancing,
## but this could easily be replaced with something more efficient.
class DisjointSet:
    def __init__(self, nodes):
        self.node_mapping = {}
        for i, val in enumerate(nodes):
            n = self.DSNode(val, i)
            self.node_mapping[val] = n

    def find(self, node):
        return self.find_node(node).parent

    def find_node(self, node):
        if type(self.node_mapping[node].parent) is int:
            return self.node_mapping[node]
        else:
            parent_node = self.find_node(self.node_mapping[node].parent.val)
            self.node_mapping[node].parent = parent_node
            return parent_node

    def union(self, node1, node2):
        parent1 = self.find_node(node1)
        parent2 = self.find_node(node2)
        if parent1.parent != parent2.parent:
            parent1.parent = parent2

    class DSNode:
        def __init__(self, val, parent):
            self.val = val
            self.parent = parent


## Kruskal's Algorithm
edges = [(node, nbor) for node in nodes for nbor in neighbors(node)]
maze = []
ds = DisjointSet(nodes)

while len(maze) < len(nodes) - 1:
    edge = edges.pop(random.randint(0, len(edges) - 1))
    if ds.find(edge[0]) != ds.find(edge[1]):
        ds.union(edge[0], edge[1])
        maze.append(edge)

## Now convert to an image
img = np.zeros((GRAPH_SIZE * (CELL_THICKNESS + WALL_THICKNESS) + WALL_THICKNESS,
                GRAPH_SIZE * (CELL_THICKNESS + WALL_THICKNESS) + WALL_THICKNESS), dtype=np.uint8)

for edge in maze:
    min_x = WALL_THICKNESS + min(edge[0][0], edge[1][0]) * (CELL_THICKNESS + WALL_THICKNESS)
    max_x = WALL_THICKNESS + max(edge[0][0], edge[1][0]) * (CELL_THICKNESS + WALL_THICKNESS)
    min_y = WALL_THICKNESS + min(edge[0][1], edge[1][1]) * (CELL_THICKNESS + WALL_THICKNESS)
    max_y = WALL_THICKNESS + max(edge[0][1], edge[1][1]) * (CELL_THICKNESS + WALL_THICKNESS)
    img[min_x:max_x + CELL_THICKNESS, min_y:max_y + CELL_THICKNESS] = 255

im = Image.fromarray(img)
im.show()

## Save maze (include extension!)
im.save(input("Save location? "))

'''
