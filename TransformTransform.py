def S(A, N):
    B = list()
    for i in range(N-1):
        for j in range(N-i-1):
            k = i + j
            if len(A[i:k]):
                B.append(max(A[i:k]))
    return B

def TransformTransform(A, N):
    L = len(S(A, N))
    B = S(A, N)
    return sum(S(B, L)) % 2 == 0
