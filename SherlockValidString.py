def FrequentFinder(lst):
    frq = 0
    num = 0
    for i in lst:
        count = lst.count(i)
        if count > frq:
            frq = count
            num = i
    return num

def SherlockValidString(s):
    letters = dict()
    for i in s:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    values = list(letters.values())
    num = FrequentFinder(values)
    pure = [int(i) for i in values if i != num]
    if len(pure) != 0:
        if (pure[0]-1 == num or pure[0]-1 == 0) and len(pure) == 1:
            return True
        else:
            return False
    else:
        return True
