'''You are given an n by n grid of distinct numbers. A number is a local
 minimum if it is smaller than all of its neighbors. (A neighbor of a
  number is one immediately above, below, to the left, or the right.
   Most numbers have four neighbors; numbers on the side have three;
   the four corners have two.) Use the divide-and-conquer algorithm design
   paradigm to compute a local minimum with only O(n) comparisons between pairs
   of numbers. (Note: since there are  numbers in the input, you cannot afford
   to look at all of them. Hint: Think about what types of recurrences would
   give you the desired upper bound.)'''

import numpy as np

def find_min_neibor(pos_x,pos_y):
    direction = []
    try:
        a = A[pos_x+1,pos_y]
        direction.append([pos_x+1,pos_y])
    except:
        a = float("inf")
        direction.append([])
    try:
        b = A[pos_x,pos_y+1]
        direction.append([pos_x,pos_y+1])
    except:
        b = float("inf")
        direction.append([])
    try:
        c = A[pos_x-1,pos_y]
        direction.append([pos_x-1,pos_y])
    except:
        c = float("inf")
        direction.append([])
    try:
        d = A[pos_x,pos_y-1]
        direction.append([pos_x,pos_y-1])
    except:
        d = float("inf")
        direction.append([])
    min_neighbor = a
    k=-1
    for i,element in enumerate([a,b,c,d]):

        if min_neighbor > element:
            min_neighbor = element
            k = i
    return min_neighbor,direction[k][0],direction[k][1]

def Isminum(pos_x,pos_y):
    min_neighbor,pos_min_x,pos_min_y = find_min_neibor(pos_x,pos_y)
    if A[pos_x,pos_y]< min_neighbor:
        return 1,[]
    else:
        return 0,[pos_min_x,pos_min_y]

def find_matrix_minum(A,pos_x ,pos_y ):
    Isminum_ans,direct = Isminum(pos_x,pos_y)
    if Isminum_ans:
        return pos_x,pos_y,A[pos_x,pos_y]
    else:
        return find_matrix_minum(A,pos_x = direct[0],pos_y = direct[1])

A = np.array([[900,100,99,98],[889,96,5,95],[887,83,83,81],[886,97,99,98]])
print(find_matrix_minum(A,int(A.shape[0]/2),int(A.shape[1]/2)))
