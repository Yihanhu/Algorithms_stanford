import time
def lis_read(file_name):
    lis = []
    with open(file_name) as f:
        for line in f:
            lis.append(int(line))
    return lis

def find_up(before_pos,num,lis):
    while True:
        if lis[before_pos] < num:
            return before_pos
        before_pos = before_pos - 1

def find_low(before_pos,num,lis):
    while True:
        if lis[before_pos] < num:
            return before_pos-1
        before_pos = before_pos - 1

start = time.clock()
lis = lis_read('algo1-programming_prob-2sum.txt')
lis = sorted(lis)
tlis = [0 for x in range(-10000,10001)]
print('loading&sorting_complete',time.clock()-start)
upper = len(lis)-1
lower = len(lis)-1
for i,num in enumerate(lis):
    print(i)
    f1 = time.clock()
    upper = find_up(upper,10000-num,lis)  #对于任意一个num，只有可能在此范围内有合格的解
    lower = find_low(lower,-10000-num,lis)
    val_set = set(lis[upper:lower])
    print(val_set)
    for t in range(-10000,10001):
        if t-num in val_set:
            tlis[t+10000] += 1
print(sum(tlis[:]==2))


print(Sum_count,time.clock()-start)
