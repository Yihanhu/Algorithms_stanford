import time
import operator

class Node():
    """docstring for Node,if it is explored,explored = True.
    out_edge is a list for out edge"""
    def __init__(self,name):
        self.name = name
        self.explored = False
        self.out_edge = []
        self.leader = None

    def append(self,head):
        self.out_edge.append(head)

    def explore(self):
        self.explored = True

    def n_print(self):
        print(self.name,self.explored)
        print(self.out_edge)

def Graph_read(file_name):
    G = {}
    G_rev = {}
    with open(file_name) as f:
        for line in f:
            words = line.split()
            if int(words[0]) not in G:
                G[int(words[0])] = Node(int(words[0]))
            if int(words[1]) not in G_rev:
                G_rev[int(words[1])] = Node(int(words[1]))
            G[int(words[0])].append(int(words[1]))
            G_rev[int(words[1])].append(int(words[0]))
    return G,G_rev

def DFS_Loop1(G): #外层循环，t在第一遍DFS中起作用，判断节点的finishing time
  #s在第二次中起作用，判断leader，即SCC节点
    global t,s,f_time,SCC_Num_lis
    t = 0
    s = None
    name_lis = [node for node in G]
    #print(sorted(name_lis,reverse = True))
    f_time = {}
    for i in sorted(name_lis,reverse = True):
        if not G[i].explored:
            #print(i)
            #print(i)
            DFS_Stack(G,i)

def DFS_Loop2(G): #外层循环，t在第一遍DFS中起作用，判断节点的finishing time
  #s在第二次中起作用，判断leader，即SCC节点头
    global t,s,f_time,SCC_Num_lis
    s = None
    SCC_Num_lis = {} #统计leader s中节点的个数
    #print(f_time)
    sorted_x = sorted(f_time.items(), key=operator.itemgetter(1),reverse = True)
    #print(sorted_x)
    #按照f_time中value降序排序
    for i,f_time_num in sorted_x:
        #print(i,f_time_num)
        #print(i,00000)
        if i not in G:
            G[i] = Node(i)
            s = i
            DFS_Stack(G,i)
        else:
            if not G[i].explored:
                #print(123)
                s = i
                DFS_Stack(G,i)

'''def DFS(G,i):
    global t,s,f_time,SCC_Num_lis
    G[i].explore()
    G[i].leader = s
    if s != None:
        SCC_Num_lis[s] = SCC_Num_lis.get(s,0)+1
    for j in G[i].out_edge:
        if j in G and not G[j].explored:
             DFS(G,j)
        t = t + 1     #弹栈的视乎时间加一
        f_time[i] = t #记录时间'''

def DFS_Stack(G,i):
    global t,s,f_time,SCC_Num_lis
    #print(s)
    Stack = []
    Stack.append(i)
    while len(Stack)>0:
        #print(s,len(Stack))
        while True: #疯狂压栈
            #print(Stack)
            num = Stack.pop()
            Stack.append(num)
            G[num].explore()
            explore_left = False
            #print(len(Stack),num,G[num].out_edge)
            for j in G[num].out_edge:
                #print(len(Stack))
                #print(0,j)
                if j in G :
                    if not G[j].explored:
                        Stack.append(j)
                        G[j].explore()
                        #print(1)
                        explore_left = True
                        #print('sadasdasd',111111111111111)
                else:
                    G[j] = Node(j)
                    Stack.append(j)
                    G[j].explore()
                    #print(2)
                    explore_left = True
                    #print(explore_left,2222222222222222222222)
            if not explore_left:
                #print('break')
                break
        '''压栈结束！'''
        num = Stack.pop() #弹栈访问
        G[num].leader = s
        #print(num,t)
        #print(s)
        if s != None:
            SCC_Num_lis[s] = SCC_Num_lis.get(s,0)+1
        #else:
        #    print(i,t,1111)
            #print(SCC_Num_lis)
        else:
            t = t + 1     #弹栈的视乎时间加一
            f_time[num] = t #记录时间


tic = time.clock()
global t,s,f_time,SCC_Num_lis
#G = Graph_read('SCC.txt')
G,G_rev = Graph_read('SCC.txt') #同时读出G和arc反转
print(time.clock()-tic)
print('Loading Complete')
print('''begin DFS_search''')
DFS_Loop1(G_rev)
print(time.clock()-tic)
print('DFS_Loop1 Complete')
DFS_Loop2(G)
print(time.clock()-tic)
print('DFS_Loop2 Complete')
#print(SCC_Num_lis)
sorted_SCC = sorted(SCC_Num_lis.values(),reverse = True)
#再一次按value降序排列
print('Top 5:')
print(sorted_SCC[:5])
#for name,node in G.items():
#    node.n_print()
print(time.clock()-tic)
