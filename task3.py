def ConquestCampaign(N, M, L, battalion):
    if N*M == 0:
        return 0
    elif N*M <= L:
        return 1
        
    # инициализация поля боя для захвата
    battlefield = [[0 for j in range(M)] for i in range(N)]
    
    # высадка первых войск
    days = 1
    fields = N*M
    for i in range(0, len(battalion), 2):
        line = battalion[i] - 1
        column = battalion[i+1] - 1
        battlefield[line][column] = days
        fields -= 1
    
    
    # захват территории
    while fields:
        days += 1
        for i in range(len(battlefield)):
            for j in range(len(battlefield[i])):
                if battlefield[i][j] == days-1:
                    if i-1 >= 0:
                        if battlefield[i-1][j] == 0:
                            battlefield[i-1][j] = days
                            fields -= 1
                    if i+1 < N:
                        if battlefield[i+1][j] == 0:
                            battlefield[i+1][j] = days
                            fields -= 1
                    if j-1 >= 0:
                        if battlefield[i][j-1] == 0:
                            battlefield[i][j-1] = days
                            fields -= 1
                    if j+1 < M:
                        if battlefield[i][j+1] == 0:
                            battlefield[i][j+1] = days
                            fields -= 1

    return days
