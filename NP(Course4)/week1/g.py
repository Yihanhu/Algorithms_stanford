import numpy as np
import heapq as h
import time


class Johnson():
    def __init__(self, txt_name):
        with open(txt_name) as f:
            f_lis = f.readlines()
            self.v_num = int(f_lis[0].split()[0])
            self.e_num = int(f_lis[0].split()[1])
            self.G = {}
            self.G_re = {}
            for g_txt in f_lis[1:]:
                tail = int(g_txt.split()[0])
                head = int(g_txt.split()[1])
                edge_l = int(g_txt.split()[2])
                if head not in self.G.keys():
                    self.G[head] = []
                self.G[head].append((tail, edge_l))

    def run_BF(self):
        self.BF = self.G
        for i in range(1, self.v_num + 1):
            self.BF[i].append((self.v_num + 1, 0))
        self.A = np.inf * np.ones((self.v_num + 1,))
        self.A_next = np.zeros((self.v_num + 1,))
        self.A[self.v_num] = 0
        for i in range(1, self.v_num + 2):  # the recurrence for <=i num of edges
            for v in range(1, self.v_num + 1):  # the recurrence for name i vertice
                cache = []
                cache.append(self.A[v - 1])
                # print(self.BF[v])
                for tail, edge_l in self.BF[v]:
                    cache.append(edge_l + self.A[tail - 1])
                self.A_next[v - 1] = min(cache)
            if i != (self.v_num + 1):
                for m in range(len(self.A)):
                    self.A[m] = self.A_next[m]
        for i in range(self.v_num):
            # print(self.A[i], self.A_next[i])
            if self.A[i] != self.A_next[i]:
                print('Negative cycle!')

    def reweight(self):
        point_weight = self.A
        # print(point_weight)
        # print(self.A_next)
        self.G_re = {}
        for head, edges in self.G.items():
            for tail, edge_l in edges:
                # print(type(point_weight[tail - 1]))
                edge_lnew = int(edge_l + point_weight[tail - 1] - point_weight[head - 1])
                # print(tail,head)
                # print('new_edge:', edge_lnew)
                # print(type(edge_lnew))
                # print(tail)
                if tail not in self.G_re.keys():
                    self.G_re[tail] = []
                    self.G_re[tail].append((edge_lnew, head))
                else:
                    self.G_re[tail].append((edge_lnew, head))

    def Dij(self):
        point_weight = self.A
        min_lis = np.inf * np.ones(((self.v_num,)))
        for v in range(self.v_num):  # recurrently compute the shortest path of each vertices
            length = np.inf * np.ones((self.v_num,))
            conqur_vertices = [v]
            length[v] = 0
            heap = []
            for edge_l, head in self.G_re[v + 1]:
                heap.append((edge_l, head))
            h.heapify(heap)
            while len(conqur_vertices) != self.v_num:
                min_l, min_head = h.heappop(heap)
                conqur_vertices.append(min_head - 1)
                length[min_head - 1] = min_l
                for edge_l, head in self.G_re[min_head]:
                    if (head - 1) not in conqur_vertices:
                        h.heappush(heap, min((length[head - 1], head), (int(edge_l + length[min_head - 1]), head)))
            for m in range(self.v_num):
                length[m] = length[m] + point_weight[m] - point_weight[v]
            min_lis[v] = np.min(length)
        min_min = np.min(min_lis)
        print('result:', min_min)


start = time.time()
solver = Johnson('g3.txt')
end1 = time.time()
print('time:', end1 - start)

solver.run_BF()
end2 = time.time()
print('time:', end2 - start)
solver.reweight()
end3 = time.time()
print('time:', end3 - start)
solver.Dij()
end4 = time.time()
print('time:', end4 - start)
