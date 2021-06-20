class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_branch(root, min_data, max_data, frequency):
    if not root:
        return True

    if frequency.get(root.data):
        return False
    else:
        frequency[root.data] = True

    if (min_data and root.data <= min_data) or (max_data and root.data >= max_data):
        return False

    if (
        not check_branch(root.left, min_data, root.data, frequency) or 
        not check_branch(root.right, root.data, max_data, frequency)
    ):
        return False

    return True

def checkBST(root):
    frequency = {}
    return check_branch(root, None, None, frequency)


if __name__ == "__main__":
    a = Node(17)
    b = Node(8)
    c = Node(24)
    d = Node(22)
    e = Node(25)
    f = Node(16)
    g = Node(23)
    print(checkBST(a))
    