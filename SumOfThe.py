def SumOfThe(N, data):
    ind = [int(k) for k in range(N)]
    for i in range(N):
        ind_lst = ind.copy()
        ind_lst.remove(i)
        sum_nums = 0
        for j in ind_lst:
            sum_nums += data[j]
        if data[i] == sum_nums:
            return data[i]
