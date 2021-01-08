def Football(F, N):
    k = 0
    for i in range(N-1):
        for j in range(k, N):
            f = F[:]
            if i != j:
                f[i], f[j] = f[j], f[i]
            if f == sorted(F[:]) or f == sorted(F[::-1]):
                return True
        k += 1
    return False
