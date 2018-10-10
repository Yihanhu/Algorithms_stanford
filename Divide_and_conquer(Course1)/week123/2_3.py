'''You are given a sorted (from smallest to largest) array A of n distinct
integers which can be positive, negative, or zero. You want to decide whether
or not there is an index i such that A[i] = i. Design the fastest algorithm
that you can for solving this problem.'''

def sorted_pair_search(lst):
    n = len(lst)
    if n == 1:
        return 0
    if lst[int(n/2)]>int(n/2):
        return sorted_pair_search(lst[:int(n/2)])
    if lst[int(n/2)]<int(n/2):
        return sorted_pair_search(lst[int(n/2)+1:])
    else:
        return 1

a = sorted_pair_search([-1,0,1,5,6,7,8])
print(a)
