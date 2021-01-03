def ListConv(tree, toList):
    mtx = list()
    if toList:
        for i in tree:
            mtx.append(list(i))
    else:
        for i in tree:
            mtx.append(''.join([str(j) for j in i]))
    return mtx

def TreeOfLife(H, W, N, tree):
    tree = ListConv(tree, True)
    for i in range(1, N+1):
        for n in range(H):
            for m in range(W):
                if tree[n][m] == '.':
                    tree[n][m] = 1
                elif tree[n][m] == '+':
                    tree[n][m] = 2
                else:
                    tree[n][m] = tree[n][m] + 1
        if i % 2 == 0:
            for n in range(H):
                for m in range(W):
                    if tree[n][m] != '.':
                        if tree[n][m] >= 3:
                            tree[n][m] = '.'
                            if n > 0:
                                if tree[n-1][m] != '.':
                                    if tree[n-1][m] <= 2:
                                        tree[n-1][m] = '.'
                            if n < H-1:
                                if tree[n+1][m] != '.':
                                    if tree[n+1][m] <= 2:
                                        tree[n+1][m] = '.'
                            if m > 0:
                                if tree[n][m-1] != '.':
                                    if tree[n][m-1] <= 2:
                                        tree[n][m-1] = '.'
                            if m < W-1:
                                if tree[n][m+1] != '.':
                                    if tree[n][m+1] <= 2:
                                        tree[n][m+1] = '.'
    tree = ListConv(tree, False)
    return tree
