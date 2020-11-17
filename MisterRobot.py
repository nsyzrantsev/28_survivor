# https://skillsmart.ru/algo/lvl1/f8c6.html

def NotSortedData(data):
    if data == sorted(data.copy()):
        return False
    return True

def MisterRobot(N, data):
    i = 0
    while NotSortedData(data):
        i = 0
        for j in range(3,N+1):
            triplet = data[i:j]
            if NotSortedData(triplet):
                for _ in range(3):
                    triplet = [triplet[1], triplet[2], triplet[0]]
                    if not NotSortedData(triplet):
                        break
            data[i:j] = triplet[:]
            if NotSortedData(triplet):
                return False
            if not NotSortedData(data):
                return True
            i += 1
