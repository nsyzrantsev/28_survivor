# https://skillsmart.ru/algo/lvl1/f70a.html
class Rings:
    def __init__(self, N):
        self.N = N
        self.result = list()
    
    def rings_gen(self, ring):
        rings_lst = ring[:]
        if ring.count('(') < self.N:
            for i in range(1, len(ring)+3):
                rings_lst.insert(i-1, '(')
                rings_lst.insert(i, ')')
                ring_line = ''.join(rings_lst)
                if rings_lst.count('(') == self.N and ring_line not in self.result:
                    self.result.append(ring_line)
                self.rings_gen(rings_lst)
                rings_lst = ring[:]
        return ' '.join(self.result)

def BalancedParentheses(N):
    ring = Rings(N)
    return ring.rings_gen(['(', ')'])
