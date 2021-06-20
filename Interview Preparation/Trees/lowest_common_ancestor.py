def lca(root, v1, v2):
    while root:
        if v1 <= root.info <= v2 or v1 >= root.info >= v2:
            return root
        elif v1 > root.info:
            root  = root.right
        else:
            root = root.left
    