# https://skillsmart.ru/algo/lvl1/d83i.html

def MatrixTurn(Matrix, M, N, T):
    result = [[None for i in range(N)] for _ in range(M)]
    current = 0
    for t in range(T):
        k = 0
        l = 0
        count = 0
        while count < N*M:
            for i in range(k, M-k):
                for j in range(l, N-l):
                    if (i == k or i not in (k, M-k-1)) and j == l:
                        result[i][j] = Matrix[i+1][j]
                        count += 1
                    elif i == k and j > l:
                        result[i][j] = Matrix[i][j-1]
                        count += 1
                    elif (i not in (k, M-k-1) or i == M-k-1) and j == N-l-1:
                        result[i][j] = Matrix[i-1][j]
                        count += 1 
                    elif i == M-k-1 and j < N-l-1:
                        result[i][j] = Matrix[i][j+1]
                        count += 1
            k += 1
            l += 1
        
        for i in range(M):
            line = ''
            for j in range(N):
                line += result[i][j]
            Matrix[i] = line
