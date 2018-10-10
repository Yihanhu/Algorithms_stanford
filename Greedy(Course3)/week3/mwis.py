import numpy as np


class mwis:
    def __init__(self, txt_name):
        self.txt_name = txt_name

    def read_file(self):
        with open(self.txt_name) as f:
            f_lis = f.readlines()
        self.v_num = int(f_lis[0])
        self.weight = [int(f_lis[i]) for i in range(1,self.v_num+1)]

    def solve(self):
        self.A = np.zeros((self.v_num + 1,))
        self.A[0] = 0
        self.A[1] = self.weight[0]
        for i in range(2, self.v_num + 1):
            self.A[i] = max(self.A[i - 1], self.A[i - 2] + self.weight[i-1])

    def solve_vertices(self):
        self.S = np.zeros((self.v_num,))
        i = self.v_num
        while i >= 1:
            if self.A[i] > self.A[i - 1]:
                self.S[i - 1] = 1
                i = i - 2
            else:
                i = i - 1


solver = mwis('mwis.txt')
solver.read_file()
solver.solve()
solver.solve_vertices()
print(solver.S)
print(solver.S[[0, 1, 2, 3, 16, 116, 516, 996]])
