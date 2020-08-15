class Battle:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.battlefield = [[0 for j in range(M)] for i in range(N)]
        self.day = 0
        self.free = N*M

    def start(self, battalion):
        self.day = 1
        for i in range(0, len(battalion), 2):
            line = battalion[i] - 1
            column = battalion[i+1] - 1
            if self.battlefield[line][column] == 0:
                self.battlefield[line][column] = 1
                self.free -= 1
    
    def run(self):
        while self.free != 0:
            self.day += 1
            for x, line in enumerate(self.battlefield):
                for y, value in enumerate(line):
                    if value == self.day - 1:
                        self.step(x, y)
        return self.day
    
    def step(self, x, y):
        self.step_to_point(x-1, y)
        self.step_to_point(x+1, y)
        self.step_to_point(x, y-1)
        self.step_to_point(x, y+1)

    def step_to_point(self, x, y):
        if x >= 0 and x < self.N and y >= 0 and y < self.M:
            if self.battlefield[x][y] == 0:
                self.battlefield[x][y] = self.day
                self.free -= 1

def ConquestCampaign(N, M, L, battalion):
    battle = Battle(N, M)
    battle.start(battalion)

    return battle.run()

