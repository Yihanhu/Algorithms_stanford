import heapq as h
with open('edges.txt','r') as f:
    n = 0
    G = {}
    for line in f:
        if n == 0 :
            num_V = int(line.split()[0])
            num_E = int(line.split()[1])
            n += 1
        else:
            v1 = int(line.split()[0])
            v2 = int(line.split()[1])
            cost = int(line.split()[2])
            dic = G.get(v1,[])
            dic.append((v2,cost))
            G[v1] = dic
            dic = G.get(v2,[])
            dic.append((v1,cost))
            G[v2] = dic
# print(G)

s = 1
X = []
X.append(s)
total_cost = 0
heap = []
# initialize
for edge in G[s]:
    v = edge[0]
    cost = edge[1]
    h.heappush(heap,(cost,s,v))
# began
flag = True
while len(heap) != 0:
    while True:
        cost,s,v = h.heappop(heap)
        if len(heap) == 0:
            flag = 0
            break
        if v not in X:
            break
    if not flag:
        break
    X.append(v)
    total_cost += cost
    for edge in G[v]:
        v2 = edge[0]
        cost2 = edge[1]
        if v2 not in X:
            h.heappush(heap,(cost2,v,v2))
print(sum(sorted(X)))
print(total_cost)
