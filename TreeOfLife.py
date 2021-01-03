def ListConv(tree, toList):
    mtx = list()
    for i in tree:
        if toList:
            mtx.append(list(i))
        else:
            mtx.append(''.join([str(j) for j in i]))
    return mtx

def TreeDeath(n, m, H, W, tree):
    if n >= 0 and n < H and m >= 0 and m < W:
        if tree[n][m] != '.':
            if tree[n][m] <= 2:
                tree[n][m] = '.'
    return tree

# year of destroy
def Destroy(tree, H, W):
    for n in range(H):
        for m in range(W):
            if tree[n][m] != '.':
                if tree[n][m] >= 3:
                    tree[n][m] = '.'
                    tree = TreeDeath(n+1, m, H, W, tree)
                    tree = TreeDeath(n-1, m, H, W, tree)
                    tree = TreeDeath(n, m+1, H, W, tree)
                    tree = TreeDeath(n, m-1, H, W, tree)
    return tree

# year of growth
def Growth(tree, H, W):
    for n in range(H):
        for m in range(W):
            if tree[n][m] == '.':
                tree[n][m] = 1
            elif tree[n][m] == '+':
                tree[n][m] = 2
            else:
                tree[n][m] = tree[n][m] + 1
    return tree

def TreeOfLife(H, W, N, tree):
    tree = ListConv(tree, True)
    for i in range(1, N+1):
        tree = Growth(tree, H, W)
        if i % 2 == 0:
            tree = Destroy(tree, H, W)
    return ListConv(tree, False)
