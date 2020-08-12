def squirrel(N):
    if N < 0:
        return 'Integer is not positive!'
    factorial = 1
    while N > 0:
        factorial *= N
        N -= 1
    first_num = int(str(factorial)[0])
    return first_num
