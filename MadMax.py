class Interceptor:

    def __init__(self, N):
        self.N = N
        self.max_num = 0
    
    def max_number(self, Tele):
        for i in Tele:
            if i >= self.max_num:
                self.max_num = i

        return self.max_num

    def sort(self, Tele):
        for i in range(1, len(Tele)):
            key = Tele[i]
            j = i - 1
            while j >= 0 and Tele[j] > key:
                key = Tele[j+1]
                Tele[j+1] = Tele[j]
                Tele[j] = key
                j -= 1

        return Tele


    def impulse_generator(self, Tele):
        max_num = self.max_number(Tele)
        sorted_array = self.sort(Tele)
        middle = self.N // 2
        current = 0
        j = self.N - 1
        for i in range(middle, self.N-2):
            current = Tele[i]
            Tele[i] = Tele[j]
            Tele[j] = current
            j -= 1

        return Tele

def MadMax(N, Tele):
    car = Interceptor(N)

    return car.impulse_generator(Tele)
