def ConquestCampaign(N, M, L, battalion):
    if N*M == 0:
        return 0
    elif N*M == L:
        return 1
    
    # инициализация поля захвата
    matrix = [[0 for j in range(M)] for i in range(N)]
    
    # высадка первых войск
    day = 1
    count = 0
    for i in range(0, L+1, 2):
        line = battalion[i] - 1
        column = battalion[i+1] - 1
        matrix[line][column] = day
        count += 1
    
    
    # захват территории
    while True:
        if count == N*M:
            break
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == day:
                    if i > 0:
                        if matrix[i-1][j] == 0:
                            matrix[i-1][j] = day + 1
                            count += 1
                    if i >= 0 and i < N-1:
                        if matrix[i+1][j] == 0:
                            matrix[i+1][j] = day + 1
                            count += 1
                    if j > 0:
                        if matrix[i][j-1] == 0:
                            matrix[i][j-1] = day + 1
                            count += 1
                    if j >= 0 and j < M-1:
                        if matrix[i][j+1] == 0:
                            matrix[i][j+1] = day + 1
                            count += 1
        day += 1
    
    return day
