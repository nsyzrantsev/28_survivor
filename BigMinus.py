# https://skillsmart.ru/algo/lvl1/s81f.html

def BigMinus(s1, s2):
    rem = 0
    sub = ''
    long = len(s1)
    short = len(s2)
    if len(s2) > len(s1):
        long, short = short, long
        s1, s2 = s2, s1
    zeros = '0'*(long-short)
    s2 = zeros+s2
    for i in range(long):
        num = int(s1[long-1-i]) - int(s2[long-1-i]) + rem
        if num < 0:
            rem = -1
            num *= -1
        else:
            rem = 0
        sub += str(num)
    sub = sub[::-1]
    return sub
