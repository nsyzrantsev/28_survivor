# https://skillsmart.ru/algo/lvl1/off8.html

def TankRush(H1, W1, S1, H2, W2, S2):
    S1 = S1.split()
    for i in range(H1 - H2 + 1):
        line = ''
        for j in range(W1 - W2 + 1):
            for e in range(H2):
                line += S1[e+i][j:j+W2] + " "
        if S2 in line:
            return True
    return False
