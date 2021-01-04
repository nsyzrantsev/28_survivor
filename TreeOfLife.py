def listConv(tree, toList):
    mtx = list()
    for row in tree:
        if toList:
            line = row.replace('+', '1')
            line = line.replace('.', '0')
            mtx.append([int(i) for i in line])
        else:
            line = ''
            for cell in row:
                if cell > 0:
                    line += '+'
                else:
                    line += '.'
            mtx.append(line)
    return mtx

def TreeReload(n, m, H, W, tree):
    if n >= 0 and n < H and m >= 0 and m < W:
        if tree[n][m] <= 2:
            tree[n][m] = 0
    return tree

# year of destroy
def Destroy(tree, H, W):
    for n in range(H):
        for m in range(W):
            if tree[n][m] >= 3:
                tree[n][m] = 0
                tree = TreeReload(n+1, m, H, W, tree)
                tree = TreeReload(n-1, m, H, W, tree)
                tree = TreeReload(n, m+1, H, W, tree)
                tree = TreeReload(n, m-1, H, W, tree)
    return tree

# year of growth
def Growth(tree, H, W):
    for n in range(H):
        for m in range(W):
            tree[n][m] = tree[n][m] + 1
    return tree

def TreeOfLife(H, W, N, tree):
    tree = listConv(tree, True)
    for i in range(1, N+1):
        tree = Growth(tree, H, W)
        if i % 2 == 0:
            tree = Destroy(tree, H, W)
    return listConv(tree, False)
