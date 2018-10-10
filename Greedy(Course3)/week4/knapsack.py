import numpy as np


class knapsack:
    def __init__(self, txt_name):
        with open(txt_name) as f:
            f_lis = f.readlines()
            self.size = int(f_lis[0].split()[0])
            self.num = int(f_lis[0].split()[1])
            self.values = [int(i.split()[0]) for i in f_lis[1:]]
            self.weights = [int(i.split()[1]) for i in f_lis[1:]]
            self.A = np.zeros((self.num,self.size))

    def run(self):
        for i in range(1, self.num):
            for w in range(self.size):
                weight = self.weights[i]
                value = self.values[i]
                if w - weight >= 0:
                    self.A[i, w] = max(self.A[i - 1, w], self.A[i - 1, w - weight]+value)
                else:
                    self.A[i, w] = self.A[i - 1, w]


solver = knapsack('knapsack1.txt')
solver.run()
print(solver.A)
print(solver.A[solver.num - 1, solver.size - 1])
