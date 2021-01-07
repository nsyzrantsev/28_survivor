def S(A, N):
    B = list()
    for i in range(N):
        for j in range(N-i):
            k = i + j
            if len(A[j:k]):
                B.append(max(A[j:k]))
    return B

def TransformTransform(A, N):
    L = len(S(A, N))
    B = S(A, N)
    return sum(S(B, L)) % 2 == 0
