class Combinator:
    result = list()
    def combs(self, inp, j=0, start=1):
        line = list(inp)
        for i in range(start, len(line)):
            self.combs(line, j+1, start+1)
            line[j], line[i] = line[i], line[j]
            if ''.join(line) not in Combinator.result:
                Combinator.result.append(''.join(line))
            self.combs(line, j+1, start+1)
            line = list(inp)
        return Combinator.result

def BiggerGreater(inp):
    Combinator.result.append(inp)
    comb = Combinator()
    comb.combs(inp)
    words = sorted(Combinator.result)
    if len(words) > 1:
        index = words.index(inp)
        if index < len(words)-1:
            return words[words.index(inp)+1]
    return ''
