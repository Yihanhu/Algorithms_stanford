with open('jobs.txt','r') as f:
    n = 0
    lis = []
    for line in f:
        if n == 0:
            n += 1
            total = int(line)
            continue
        else:
            lis.append((int(line.split()[0]) - int(line.split()[1]) , \
            int(line.split()[0]) , int(line.split()[1])))
            # first is  weight- length, accend sorting,  second is weight, accend sorting , third is length
lis = sorted(lis)
sum = 0
time = 0
for i in range(total-1,-1,-1):
    weight =  lis[i][1]
    len = lis[i][2]
    time = time + len
    sum = sum + (time) * weight
print(sum)
