# https://skillsmart.ru/algo/lvl1/6d4d.html

def WordsCutter(a, l):
    text = a.split()
    lst_words = list()
    for i,v in enumerate(text):
        while len(v) > l:
            lst_words.append(v[0:l])
            v = v[l:]
        lst_words.append(v+' ')
    return lst_words

def TextAlignment(words, l):
    result = list()
    line = words[0]
    if len(words) == 1 and len(line[:-1]) <= l:
        result.append(line[:-1])
        return result
    lst = words[1:]
    for i, e in enumerate(lst):
        if len(line+e[:-1]) <= l:
            line += e
            continue
        else:
            if line[-1] == ' ':
                line = line[:-1]
            result.append(line)
            line = e
            if i == len(lst)-1:
                if line[-1] == ' ':
                    line = line[:-1]
                result.append(line)
    return result

def WordSearch(length, s, subs):
    formated = WordsCutter(s, length)
    print(formated)
    text = TextAlignment(formated, length)
    print(text)
    result = [0]*len(text)
    for i, string in enumerate(text):    
        if subs in string.split():
            result[i] = 1
    return result
