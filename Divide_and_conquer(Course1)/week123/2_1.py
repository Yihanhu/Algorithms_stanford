def find2small(lst):
    '''原理首先用迭代法(recurssive calls)解出最大值，沿途记录最大值
    击败的对手(logn)，最后直接找出logn对手中最大的即可，总共对比次数为n+logn-2'''

    def find_greatest(gre_lst):
        n = len(gre_lst)
        if n == 1:
            return gre_lst[0],[]
        max1,lst1 = find_greatest(gre_lst[:int(n/2)])
        max2,lst2 = find_greatest(gre_lst[int(n/2):])
        if max1 > max2:
            lst1.append(max2) #创建被打败的list,每一位胜者都会把击败的对手放进list，直到自己被击败，list清空
            return max1,lst1
        else:
            lst2.append(max1)
            return max2,lst2
    '''到此，总复杂度为n-1'''

    max_num, beaten_list= find_greatest(lst)
    second_max = beaten_list[0]
    for element in beaten_list[1:]:
        if second_max < element:
            second_max = element
    '''复杂度logn-1'''
    return second_max

a = find2small([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(a)
