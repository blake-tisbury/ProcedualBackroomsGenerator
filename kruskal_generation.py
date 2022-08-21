import random


class DisjointSet:
    # TODO: add rank balancing to union function and path compression to find function to reduce time complexity
    def __init__(self, nodes):
        self.parent = {}

        # initialize each node to itself as the parent, creating "i" number of disjoint sets
        for i in nodes:
            self.parent[i] = i

    def find(self, node):
        # if "node" is the parent of itself, return "node"
        if self.parent[node] == node:
            return node
        else:
            # otherwise, recursively find the parent of "node"'s parent
            return self.find(self.parent[node])

    def union(self, node1, node2):
        # find the parent of each node
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        # if they're not the same, make node1's parent node2's parent, this seems kind of redundant but,
        # maybe it will save a few copy operations?
        # TODO: check if this is actually faster than just doing the union operation
        if parent1 != parent2:
            self.parent[parent1] = parent2


# Kruskal's Algorithm
def random_kruskal_maze(size):
    maze = []
    nodes = generate_nodes(size)
    edges = [(node, nbor) for node in nodes for nbor in generate_neighbors(node, size)]
    ds = DisjointSet(nodes)

    while len(maze) < len(nodes) - 1:
        # pick a random edge
        edge = edges.pop(random.randint(0, len(edges) - 1))
        # if the two nodes are not in the same set, union them and add the edge to the maze
        if ds.find(edge[0]) != ds.find(edge[1]):
            ds.union(edge[0], edge[1])
            maze.append(edge)

    return maze


def generate_nodes(size):
    return [(i, j) for j in range(size) for i in range(size)]


def generate_neighbors(node, size):
    return [(node[0] + dx, node[1] + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if 0 <= node[0] + dx < size and 0 <= node[1] + dy < size]


