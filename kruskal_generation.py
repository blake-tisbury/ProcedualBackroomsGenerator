class DisjointSet:
    # TODO: Add rank balancing to union function and path compression to find function to reduce time complexity
    def __init__(self, nodes):
        self.parent = {}

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
