def StringSeparator(string):
    line = ''
    separated_str = string.split(' ')


    for i, value in enumerate(string):
        if i == len(string) - 1:
            line += value
            separated_str.append(line)
        else:
            if len(line) != 0 and value == ' ':
                separated_str.append(line)
                separated_str.append(value)
                line = ''
            elif value == ' ':
                separated_str.append(value)
            else:
                line += value
    return separated_str

def WordSeparator(l, string):
    lst = StringSeparator(string)
    print(lst)
    sep_lst = list()
    line = ''
    start = 0

    for i, value in enumerate(lst):
        if i == len(lst)-1:
            sep_lst.append(line+value)
        if len(value) > l:
            sep_lst.append(value[0:l])
            line = value[l:]
        elif len(line + value) <= l:
            line += value
        else:
            sep_lst.append(line)
            line = value

    return sep_lst
            

def WordSearch(l, string, subs):
    sep_lst = WordSeparator(l, string)
    print(sep_lst)
    result = list()
    for e, value in enumerate(sep_lst):
        word = ''
        count = 0
        for i, letter in enumerate(value):
            if len(word) != 0 and (letter == ' ' or i == len(value)-1):
                if word == subs:
                    count += 1
                word = ''
            elif letter != ' ':
                word += letter
        if count:
            for i in range(count):
                result.append(1)
        else:
            result.append(0)
    return result

line = 'Пустые строк строк в такой разбивке полностью исключаются. Если ширина разбивки меньше какого-то слова, то это слово разбиваешься строк на несколько'

print(WordSearch(3, '12345', '123'))
