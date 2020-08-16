from math import sqrt

class Unlock:
    def __init__(self, N):
        self.N = N
        self.layout = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
        self.seq_y = [0]*N
        self.seq_x = [0]*N
        self.length = 0

    def xy_positions(self, hits):
        layout = self.layout
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                if layout[i][j] in hits:
                    index = hits.index(layout[i][j])
                    self.seq_y[index] = i
                    self.seq_x[index] = j
    
    def length_sequence(self, hits):
        self.xy_positions(hits)
        seq_y = self.seq_y
        seq_x = self.seq_x

        for i in range(1, self.N):
            if seq_y[i] - seq_y[i-1] == 0 or seq_x[i] - seq_x[i-1] == 0:
                len_points = 1
            else:
                len_points = sqrt((seq_y[i]-seq_y[i-1])**2 + (seq_x[i]-seq_x[i-1])**2)
            self.length += len_points
        return self.length

def PatternUnlock(N, hits) -> str:
    unlock = Unlock(N)
    length = unlock.length_sequence(hits)
    result = str(int(round(length, 5)*100000)).strip('0')
    return result

print(PatternUnlock(3, [2, 1, 9]))
