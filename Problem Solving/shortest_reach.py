class Tree:

    def __init__(self) -> None:
        self.root:Node = None
        self.nodes = {}

    @classmethod
    def build(cls, edges, root_value, m):
        tree = Tree()
        for key, (i, j) in enumerate(edges):
            if key == m:
                break

            if not tree.nodes.get(i):
                tree.nodes[i] = Node(i)

            if not tree.nodes.get(j):
                tree.nodes[j] = Node(j)

            tree.nodes[i].add_child(tree.nodes[j])
            tree.nodes[j].add_child(tree.nodes[i])
            if i == root_value:
                tree.root = tree.nodes[i]
            elif j == root_value:
                tree.root = tree.nodes[j]

        return tree

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False

    def add_child(self, node):
        self.children.append(node)


def bfs(n, m, edges, s):
    tree:Tree = Tree.build(edges, s, m)
    array = [tree.root, None]
    tree.root.visited = True
    height = 6
    distances = [-1]*(n-1)
    while array:
        current = array.pop(0)
        if not current:
            if not array:
                break
            height += 6
            array.append(None)
            current = array.pop(0)

        for node in current.children:
            if not node.visited:
                node.visited =True
                if node.value > s:
                    distances[node.value-2] = height
                else:
                    distances[node.value-1] = height
                array.append(node)

    
    return distances


if __name__ == "__main__":
    matrix = [[2,3]]
    print(bfs(3,1, matrix, 2))
