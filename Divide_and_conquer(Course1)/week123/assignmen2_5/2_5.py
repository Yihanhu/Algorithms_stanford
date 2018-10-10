def CountInversions(lst):
    n = len(lst)
    if n == 1:
        return lst,0
    half = int(n/2)
    Sorted_L,L_num = CountInversions(lst[:half])
    Sorted_R,R_num = CountInversions(lst[half:])
    Sorted_total,Cross_num = CountCrossInversions(Sorted_L,Sorted_R)
    return Sorted_total,(L_num + R_num + Cross_num)

def CountCrossInversions(Sorted_L,Sorted_R):
    n_L = len(Sorted_L)
    n_R = len(Sorted_R)
    Sorted_total = []
    Cross_num = 0
    i = 0
    k = 0
    for _ in range(n_L+n_R):
        if Sorted_L[i] > Sorted_R[k]:
            Sorted_total.append(Sorted_R[k])
            Cross_num += n_L-i
            if k <n_R-1:
                k+=1
            else:
                for element in Sorted_L[i:]:
                    Sorted_total.append(element)
                break
        else:
            Sorted_total.append(Sorted_L[i])
            if i <n_L-1:
                i+=1
            else:
                for element in Sorted_R[k:]:
                    Sorted_total.append(element)
                break
    return Sorted_total,Cross_num

handle = open('IntegerArray.txt','r')
lst = []
for line in handle:
    lst.append(int(line))
print('loading complete')
Sorted_total,ans = CountInversions(lst)
print(ans)
