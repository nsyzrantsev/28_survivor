def SynchronizingTables(N, ids, salary):
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)
    table = dict(zip(sorted_ids, sorted_salary))
    result = []
    for i in ids:
        result.append(table[i])
    return result
