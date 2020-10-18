def WordsCutter(a, l):
    text = a.split()
    lst_words = list()
    for i,v in enumerate(text):
        while len(v) > l:
            lst_words.append(v[0:l])
            v = v[l:]
        if len(v) <= l:
            if len(v) < l:
                v += ' '
            lst_words.append(v)
    return lst_words

def TextAlignment(words, l):
    line = words[0]
    lst = words[1:]
    result = list()
    for i, e in enumerate(lst):
        if len(line+e) <= l:
            line += e
            continue
        else:
            result.append(line)
            line = e
            if i == len(lst)-1:
                result.append(line)
    return result

def WordSearch(length, s, subs):
    formated_str = WordsCutter(s, length)
    text = TextAlignment(formated_str, length)
    result = [0]*(len(text))
    for i, string in enumerate(text):
        word = ''
        count = False
        for j, substr in enumerate(string):
            if j == len(string)-1:
                if word+substr == subs:
                    count = True
                    result[i] = 1
                    count = False
            if substr != ' ':
                word += substr
            elif word == subs:
                count = True
                result[i] = 1
                count = False
            
    return result
