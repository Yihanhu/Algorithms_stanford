import sys
import time 

def ParseGraph(filename):
  """Parse a graph into adjacency list format per programming Q.5

Args:
- filename: the on-disk graph representation
Returns:
- vertices = {vertex_1: [(vertex_2, weight), ...]}
"""
  vertices = {}

  for l in open(filename):
    fields = [f for f in l.split()]
    vertex = int(fields.pop(0))
    edges = [tuple([int(t) for t in f.split(',')]) for f in fields]
    vertices[vertex] = edges

  return vertices

start = time.clock()

targets = [7,37,59,82,99,115,133,165,188,197]
#          7, 37, 59, 82, 99, 115, 133 ,165, 188, 197
V = ParseGraph("DijkstraData.txt")
X = {1: True}
A = {1: 0}
Path = {}
Path[1] = [1]

while len(X) != len(V):
  min_src = 0
  min_dst = 0
  min_weight = 1000000
  for u in X:
    for v, l_uv in V[u]:
      if v in X:
        continue
      if A[u] + l_uv < min_weight:
        min_src, min_dst = u, v
        min_weight = A[u] + l_uv
        Path[v] = Path[u]+[v]
  if min_src == 0:
    print ('Found nothing to match the greedy criterion! X = %s' % X)
    sys.exit(1)
  X[min_dst] = True
  A[min_dst] = min_weight

print( [A[t] for t in targets])
print([Path[t] for t in targets])
print(time.clock()-start)
