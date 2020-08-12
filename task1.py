def squirrel(N):
    factorial = 1
    while N > 0:
        factorial *= N
        N -= 1
    first_num = int(str(factorial)[0])
    return first_num
