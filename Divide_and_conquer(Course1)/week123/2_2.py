'''You are a given a unimodal array of n distinct elements, meaning
that its entries are in increasing order up until its maximum element,
after which its elements are in decreasing order.Give an algorithm to compute
the maximum element that runs in O(log n) time.'''

def max_num_unimodal(lst):
    n = len(lst)
    if n==1:
        return lst[0]
    mid = lst[int(n/2)]
    if mid > lst[int(n/2)-1] :
        if mid > lst[int(n/2)+1]:
            return mid
        else:
            return max_num_unimodal(lst[int(n/2):])
    else:
        return max_num_unimodal(lst[:int(n/2)+1])

a = max_num_unimodal([1,2,3,4,5,6,7,8,9,8,7,6,5,3,1])
print(a)
