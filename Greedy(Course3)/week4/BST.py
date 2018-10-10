import numpy as np


class BST:
    def __init__(self, f_lis):
        self.f_lis = f_lis
        self.num = len(f_lis)
        self.A = np.zeros((self.num + 1, self.num + 1))

    def run(self):
        for s in range(self.num):
            for i in range(0, self.num - s):
                j = i + s
                # print(s,i,j)
                # print(s,i,j)
                self.A[i, j] = min(
                    [(sum(self.f_lis[i:j + 1]) + self.A[i, r - 1] + self.A[r + 1, j]) for r in range(i, j + 1)])


solver = BST([0.2, 0.05,0.17,0.1, 0.2, 0.03, 0.25])
solver.run()
print(solver.A)
