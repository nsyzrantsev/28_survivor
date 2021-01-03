class Combinator:
    def __init__(self):
        self.result = list()
    
    def combs(self, inp, s, e):
        line = list(inp)
        for i in range(s, e+1):
            line[s], line[i] = line[i], line[s]
            if ''.join(line) not in self.result:
                self.result.append(''.join(line))
            self.combs(line, s+1, e)
            line[s], line[i] = line[i], line[s]
        return self.result

def BiggerGreater(inp):
    comb = Combinator()
    comb.result.append(inp)
    e = len(inp)-1
    comb.combs(inp, 0, e)
    words = sorted(comb.result)
    if len(words) > 1 and words.index(inp) <= len(words)-2:
        return words[words.index(inp)+1]
    return ''
