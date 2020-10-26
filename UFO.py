# https://skillsmart.ru/algo/lvl1/3b3d.html

def numeral_system(data, system):
    result = list()
    for i in data:
        str_num = str(i)
        octal_num = 0
        for j, e in enumerate(str_num):
            octal_num += int(e)*system**(len(str_num)-j-1)
        result.append(octal_num)
    return result

def UFO(N, data, octal):
    result = list()
    if octal:
        result = numeral_system(data, 8)
    else:
        result = numeral_system(data, 16)
    return result
