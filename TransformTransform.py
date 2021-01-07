# https://skillsmart.ru/algo/lvl1/gc8b.html
def S(A, N):
    B = list()
    for i in range(N):
        for j in range(N-i):
            k = i + j
            if len(A[j:k+1]):
                B.append(max(A[j:k+1]))
    return B

def TransformTransform(A, N):
    B = S(A, N)
    return not sum(S(B, len(B))) % 2
