
dist_lis = []
with open('clustering1.txt') as f:
    for n,lines in enumerate(f):
        if n == 0:
            tol_num = int(lines)
            continue
        else:
            words = lines.split()
            edge1 = int(words[0])
            edge2 = int(words[1])
            cost = int(words[2])
            dist_lis.append((cost,edge1,edge2))
sorted_lis = sorted(dist_lis)
#initial
print(sorted_lis[0:100])
union_head = {}
union_lis = {}
for i in range(1,tol_num+1):
    union_lis[i] = [i]
    union_head[i] = i
clus_num = tol_num
n = 0
while clus_num > 4:
    cost,edge1,edge2 = sorted_lis[n]
    n = n + 1
    # print(cost)
    if union_head[edge1]==union_head[edge2]:
        continue
    else:
        if len(union_lis[union_head[edge1]])>len(union_lis[union_head[edge2]]):
            # append edge2 to edge1
            old_head = union_head[edge2]
            for v in union_lis[union_head[edge2]]:
                union_head[v] = union_head[edge1]
                union_lis[union_head[edge1]].append(v)
        else:
            old_head = union_head[edge1]
            for v in union_lis[union_head[edge1]]:
                union_head[v] = union_head[edge2]
                union_lis[union_head[edge2]].append(v)
        # print(union_lis)
        # print(union_head)
        # print(old_head)
        del union_lis[old_head]
        # print(len(union_lis))
        clus_num -= 1
print(union_lis)
while True:
    cost,edge1,edge2 = sorted_lis[n]
    n = n + 1
    if union_head[edge1]==union_head[edge2]:
        continue
    else:
        print(cost)
        break
