import random
import copy

def read_graph(file_name):
    with open(file_name) as f:
        Graph = {}
        Edge = {}
        vertice_num = 0
        for lines in f:
            vertice_num +=1
            words = lines.split()
            words = [int(word) for word in words]
            Graph[words[0]] = words[1:] #创建出vertices->endpoint map
            Edge[words[0]] = []
            for word in words[1:]:
                Edge[words[0]].append([words[0],word]) #所有边集合，每条边重复一次
    return Graph,Edge,vertice_num

def K_min_cut_one_loop(G_out, Edge, vertice_num):
    while vertice_num >2:
        Edge_lis = sum(Edge.values(),[])
        #print(vertice_num)
        contract_edge_num = random.randint(0,len(Edge_lis)-1) #Edge.values 重复边
        contract_edge = Edge_lis[contract_edge_num]
        #print(contract_edge)
        for temp in G_out[contract_edge[1]]:
            G_out[contract_edge[0]].append(temp) #将G_out中的节点合并
            Edge[contract_edge[0]].append([contract_edge[0],temp]) #将Edge中的节点合并
            i = 0
            #print(temp)
            for temp2 in G_out[temp]:
                if temp2== contract_edge[1]:
                    G_out[temp][i] = contract_edge[0]
                    Edge[temp][i] = [temp,contract_edge[0]]
                    #print(G_out[temp][i],Edge[temp][i])
                i = i+1
        del G_out[contract_edge[1]],Edge[contract_edge[1]]  #删除收缩节点, 相对于的重复节点变成self_loop，下一步删除
        #print(Edge[contract_edge[1]])
        #print(G_out)
        #print(Edge)
        G_out,Edge = delete_self_loop(contract_edge,G_out, Edge) #
        #print(G_out)
        #print(Edge)
        vertice_num -= 1
        #print(vertice_num)
    #print(vertice_num)
    return len(sum(Edge.values(),[]))/2

def delete_self_loop(contract_edge,G_out,Edge):
    i = 0
    while i< len(G_out[contract_edge[0]]):
        temp = G_out[contract_edge[0]][i]
        if temp == contract_edge[0]:
            del G_out[contract_edge[0]][i]
            del Edge[contract_edge[0]][i]
            #print('del')
            continue
        if temp == contract_edge[1]:
            del G_out[contract_edge[0]][i]
            del Edge[contract_edge[0]][i]
            #print('del')
            continue
        #print(G_out)
        i = i + 1
    return G_out,Edge

def  K_min_cut_mulloop(file_name,n):
    mincut = 100000
    G_out_1, Edge_1, vertice_num_1 = read_graph(file_name)
    for k in range(n):
        G_out = copy.deepcopy(G_out_1)
        Edge=copy.deepcopy(Edge_1)
        vertice_num=copy.deepcopy(vertice_num_1)
        temp = K_min_cut_one_loop(G_out, Edge, vertice_num)
        if temp < mincut:
            mincut = temp
        print(k,mincut)
    return mincut

print(K_min_cut_mulloop('kargerMinCut.txt',500))
