def read_list(file_name):
    num_lis = []
    with open(file_name) as f:
        for line in f:
            num_lis.append(int(line))
    return num_lis

class heap_max(): #大根堆
    """docstring for heap_max."""
    def __init__(self):
        self.lis = []

    def insert(self,num):
        self.lis.append(num)
        k = len(self.lis)-1
        while k != 0:
            k_next = int((k-1)/2)
            if num > self.lis[k_next]:
                temp = self.lis[k_next]
                self.lis[k_next] = num
                self.lis[k] = temp
                k = k_next
            else:
                break

    def pop(self):
        n = len(self.lis)-1
        max_num = self.lis[0]
        self.lis[0] = self.lis[n]
        num = self.lis[0]
        del self.lis[n]
        n = n -1
        k = 0
        while True:
            k_child_1 = 2*k + 1
            k_child_2 = 2*k + 2
            if k_child_1 > n:
                break
            elif k_child_2 >n:
                if self.lis[k_child_1] > num:
                    temp = self.lis[k_child_1]
                    self.lis[k_child_1]  = num
                    self.lis[k] = temp
                    break
                else:
                    break
            else:
                temp_lis = sorted([(self.lis[k_child_1],k_child_1),(self.lis[k_child_2],k_child_2),(num,k)])
                if temp_lis[2][0]==num:
                    break
                else:
                    temp = temp_lis[2][0]
                    self.lis[temp_lis[2][1]] = num
                    self.lis[k] = temp
                    k = temp_lis[2][1]
        return max_num

class heap_min():
    """docstring for heap_min."""
    def __init__(self):
        self.lis = []

    def insert(self,num):
        self.lis.append(num)
        k = len(self.lis)-1
        while k != 0:
            k_next = int((k-1)/2)
            if num < self.lis[k_next]:
                temp = self.lis[k_next]
                self.lis[k_next] = num
                self.lis[k] = temp
                k = k_next
            else:
                break

    def pop(self):
        n = len(self.lis)-1
        min_num = self.lis[0]
        self.lis[0] = self.lis[n]
        num = self.lis[0]
        del self.lis[n]
        n = n -1
        k = 0
        while True:
            k_child_1 = 2*k + 1
            k_child_2 = 2*k + 2
            if k_child_1 > n:
                break
            elif k_child_2 >n:
                if self.lis[k_child_1] < num:
                    temp = self.lis[k_child_1]
                    self.lis[k_child_1]  = num
                    self.lis[k] = temp
                    break
                else:
                    break
            else:
                temp_lis = sorted([(self.lis[k_child_1],k_child_1),(self.lis[k_child_2],k_child_2),(num,k)],reverse = True)
                if temp_lis[2][0]==num:
                    break
                else:
                    temp = temp_lis[2][0]
                    self.lis[temp_lis[2][1]] = num
                    self.lis[k] = temp
                    k = temp_lis[2][1]
        return min_num




lis = read_list('Median.txt')
sum_med = lis[0]
heap_low = heap_max() #support extract MAX,建堆
heap_high = heap_min() #support extract Min
heap_high.insert(lis[0])
for i in range(1,10000):
    if lis[i]>heap_high.lis[0]: #如果被插之前，该数大于大数堆中的最小，那么
        if i%2 ==0:      #如果查之前两队均分，那么插大数堆
            heap_high.insert(lis[i])
        else:            #如果不均分，插大堆并且弹出大堆中小根,插入小堆
            heap_high.insert(lis[i])
            heap_low.insert(heap_high.pop())
    else:
        if i%2 ==0:      #如果查之前两队均分，那么插小根堆，弹栈
            heap_low.insert(lis[i])
            heap_high.insert(heap_low.pop())
        else:
            heap_low.insert(lis[i])
    if i%2 == 0:
        med = heap_high.lis[0]
    else:
        med = heap_low.lis[0]
    sum_med = med + sum_med
    if i<50:
        print(med,sorted(lis[:i+1]))
        print(heap_high.lis)
print(sum_med%10000)
