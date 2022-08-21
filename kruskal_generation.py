import random
import cProfile
from functools import lru_cache


class DisjointSet:
    def __init__(self, nodes):
        self.parent = {}
        self.rank = {}  # stores tree depth, used for union by rank

        # initialize each node to itself as the parent, creating "i" number of disjoint sets
        for i in nodes:
            self.parent[i] = i
            self.rank[i] = 0

    @lru_cache(maxsize=None)
    def find(self, node):
        # if `node` is not the parent, recursively find its parent
        if self.parent[node] != node:
            # path compression by saving the path to the root
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # find the parent of each node
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return
        # always attach the smaller tree to the bigger one, reducing tree depth and thus time complexity
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        # rank only increases when the two sets are of equal depth
        else:
            self.parent[parent1] = parent2
            self.rank[parent1] += 1


class KruskalMaze:
    def __init__(self, size):
        self.size = size
        self.nodes = self.generate_nodes()
        self.edges = [(node, neighbor) for node in self.nodes for neighbor in self.generate_neighbors(node)]
        self.ds = DisjointSet(self.nodes)

    def generate_maze(self, completion_percentage):
        maze = []

        # I chose to shuffle beforehand rather than picking a random edge each time, due to the way list.pop() works,
        # it's much faster to always pick the last element
        random.shuffle(self.edges)

        # completion_percentage is something that I wanted to add as it allows to generate sparse but
        # maze like structures, perfect for the backrooms
        while len(maze) < len(self.nodes) - 1 or len(maze) < completion_percentage * len(self.nodes):
            # pick a random edge
            edge = self.edges.pop()
            # if the two nodes are not in the same set, union them and add the edge to the maze
            if self.ds.find(edge[0]) != self.ds.find(edge[1]):
                self.ds.union(edge[0], edge[1])
                maze.append(edge)
        return maze

    def generate_nodes(self):
        return [(i, j) for j in range(self.size) for i in range(self.size)]

    def generate_neighbors(self, node):
        return [(node[0] + dx, node[1] + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
                if 0 <= node[0] + dx < self.size and 0 <= node[1] + dy < self.size]


if __name__ == "__main__":
    kruskal_maze = KruskalMaze(1000)
    cProfile.run('kruskal_maze.generate_maze(1)')
