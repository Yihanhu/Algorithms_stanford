import heapq
import time

class Node():
    """docstring for Graph_read."""
    def __init__(self):
        self.out_edge = []
        self.dis_origin = 1000000
        self.path = []

    def append_edge(self,out_vertex,distance):
        self.out_edge.append((out_vertex,distance))

def Graph_read(file_name):
    G = {}
    with open(file_name) as f:
        for line in f:
            words = line.split()
            G[int(words[0])] = Node()
            for ver_dis in words[1:]:
                ver,dis = ver_dis.split(',')
                G[int(words[0])].append_edge(int(ver),int(dis))
    return G

def Dijkstra(origin):
    X = {} #已经被conquer的vertex
    heap = []
    X[origin] = G[origin]
    G[origin].dis_origin = 0
    G[origin].path = [origin]
    #开始建堆
    for out_vertex,distance in G[origin].out_edge:
        heap.append((distance,(origin,out_vertex)))
        #数据结构，tuple中间套tuple，注意，排序是按照tuple的第一个数进行排序
    heapq.heapify(heap)
    'begin Loop'
    while len(X) != len(G):
        while True:
            w_min_unconquer = heapq.heappop(heap)
            #这时候heap里面装的是到这个点最短距离，相当于直接是score
            if w_min_unconquer[1][1] not in X:
                break
        #print(w_min_unconquer)

        edge_dis = w_min_unconquer[0]
        vertex = w_min_unconquer[1][0]
        new_vertex = w_min_unconquer[1][1]
        new_dis = edge_dis
        G[new_vertex].dis_origin = new_dis
        G[new_vertex].path = G[vertex].path + [new_vertex]
        #完成更新
        X[new_vertex] = G[new_vertex]
        #开始构建heap
        #print(G[new_vertex].out_edge)
        for out_vertex,distance in G[new_vertex].out_edge:
            #print(out_vertex,distance)
            if out_vertex not in X:
                heapq.heappush(heap,(G[new_vertex].dis_origin + distance,(new_vertex,out_vertex))) #总结所有的dist
    return X

start = time.clock()
G = Graph_read('DijkstraData.txt')
X=Dijkstra(1)
AA = []
BB = []
for i in [7,37,59,82,99,115,133,165,188,197]:
    AA.append(X[i].dis_origin)
    BB.append(X[i].path)
print(AA,BB)
print(time.clock()-start)
