class Ring:
    def __init__(self):
        self.result = list()
        
    def rings_generation(self, ring, N):
        if not N > 1:
            self.result.append(ring)
            return ring
        self.rings_generation(f'({ring})', N-1)
        self.rings_generation(f'{ring}()', N-1)

def BalancedParentheses(N):
    rings = Ring()
    rings.rings_generation('()', N)
    return ' '.join(rings.result)
