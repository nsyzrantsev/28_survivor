# https://skillsmart.ru/algo/lvl1/ab53.html

import math

def encoder(s):
    string = s[:]
    string = ''.join(string.split())
    N = len(string)
    sq_root = math.sqrt(N)
    columns = math.ceil(sq_root)
    rows = math.floor(sq_root)
    while columns*rows < N:
        rows += 1
    matrix = list()
    line = ''
    for i in range(N):
        if len(line) == rows:
            matrix.append(line)
            line = ''
        line += string[i]
        if i == N-1:
            matrix.append(line)
    result = ['' for i in range(columns)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j] += matrix[i][j]
    return ''.join(result)

def decoder(s):
    string = s[:]
    N = len(string)
    sq_root = math.sqrt(N)
    columns = math.ceil(sq_root)
    rows = math.floor(sq_root)
    while columns*rows < N:
        rows += 1
    rem = N % rows
    lens = list()
    end = 0
    for i in range(rows):
        if i < rem:
            end += rows-1
        else:
            end += rows-rem
        lens.append(end)
    start = 0
    result = ['' for i in range(rows)]
    for i,end in enumerate(lens):
        line = string[start:end+1]
        for j,letter in enumerate(line):
            result[j] += letter
        start = end+1
    return ''.join(result)

def TheRabbitsFoot(s, encode):
    if encode:
        result = encoder(s)
    else:
        result = decoder(s)
    return result
