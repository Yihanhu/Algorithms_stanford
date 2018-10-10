import numpy as np
import sys
import time

sys.setrecursionlimit(10000)


class knapsack:
    def __init__(self, txt_name):
        with open(txt_name) as f:
            f_lis = f.readlines()
            self.size = int(f_lis[0].split()[0])
            self.num = int(f_lis[0].split()[1])
            self.values = [int(i.split()[0]) for i in f_lis[1:]]
            self.weights = [int(i.split()[1]) for i in f_lis[1:]]
            print('reading finished')
            self.A = {}
            self.need = [[] for i in range(self.num)]

    def rec_run(self, i, w):
        if i == 0:
            return 0
        if (i, w) in self.A:
            return self.A[(i, w)]
        weight = self.weights[i]
        value = self.values[i]
        if w - weight >= 0:
            self.A[(i, w)] = max(self.rec_run(i - 1, w), self.rec_run(i - 1, w - weight) + value)
            return self.A[(i, w)]
        else:
            self.A[(i, w)] = self.rec_run(i - 1, w)
            return self.A[(i, w)]

    def needed_point(self):
        self.need[self.num - 1].append((self.num - 1, self.size))
        for k in range(self.num - 2, -1, -1):
            weight = self.weights[k]
            for i, w in self.need[k + 1]:
                if w - weight >= 0:
                    if (k, w - weight) not in self.need[k]:
                        self.need[k].append((k, w - weight))
                    if (k, w) not in self.need[k]:
                        self.need[k].append((k, w))
                else:
                    if (k, w) not in self.need[k]:
                        self.need[k].append((k, w))

start = time.time()
solver = knapsack('knapsack_big.txt')
print(solver.rec_run(solver.num-1,solver.size))
print('time',time.time()-start)