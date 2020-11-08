# https://skillsmart.ru/algo/lvl1/d146.html

def LineAnalysis(line):
    result = False
    stars = line.count('*')
    points = ' '.join(line.split('*')).split()
    if len(points) == 0 and stars >= 1:
        result = True
    if len(set(points)) == 1 and stars == len(points)+1:
        result = True
    return result
