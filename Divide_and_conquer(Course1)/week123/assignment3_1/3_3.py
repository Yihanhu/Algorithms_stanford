def Quicksort(lst):
    if len(lst) < 2:
        return lst,0
    #choose pivot using three-median
    lst[0]
    lst[len(lst)-1]
    lst[int((len(lst)-1)/2)]
    if lst[0]>lst[len(lst)-1]:
        if lst[len(lst)-1]>lst[int((len(lst)-1)/2)]:
            choosen = len(lst)-1
        elif lst[0]>lst[int((len(lst)-1)/2)]:
            choosen = int((len(lst)-1)/2)
        else:
            choosen = 0
    else:
        if lst[0]>lst[int((len(lst)-1)/2)]:
            choosen = 0
        elif lst[len(lst)-1]>lst[int((len(lst)-1)/2)]:
            choosen = int((len(lst)-1)/2)
        else:
            choosen = len(lst)-1        
    #swap(lst[0],lst[choosen])
    pivot = lst[choosen]
    lst[choosen] = lst[0]
    lst[0] = pivot
    i = 1
    for j in range(1,len(lst)):
        if lst[j]<pivot:
            swap = lst[j]
            lst[j] = lst[i]
            lst[i] = swap
            #swap(lst[j],lst[i])
            i+=1
    swap = lst[0]
    lst[0] = lst[i-1]
    lst[i-1] = swap
    #swap(lst[l],lst[i-1])
    if i != 1:
        a,Ca = Quicksort(lst[:i-1])
    else:
        a,Ca = [],0
    b,Cb = Quicksort(lst[i:])
    return a+[lst[i-1]]+b,len(lst)-1+Ca+Cb

'''lst = [2,8,7,5,3,1]
new = Quicksort(lst)
print(new)'''
lst = []
handle = open('QuickSort.txt','r')
for line in handle:
    lst.append(int(line))
sorted_array,Comparision = Quicksort(lst)
print(Comparision)