import heapq

class leaves:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.parent = self.name


class huffman_tree():
    def __init__(self, leaves_num):
        self.root = None
        self.leaf = []
        for i in range(leaves_num):
            p = leaves(str(i), 0)
            self.leaf.append(p)

    def leaves_pointer(self):
        return self.leaf


class huffman:
    def __init__(self, txt_name):
        self.txt_name = txt_name

    def read_file(self):
        with open(self.txt_name) as f:
            file_lis = f.readlines()
        self.num_sym = int(file_lis[0])
        self.weight_lis = [int(m) for m in file_lis[1:]]

    def build_tree(self):
        self.tree = huffman_tree(self.num_sym)
        # print(len(self.weight_lis))
        self.h = [(self.weight_lis[i], self.tree.leaves_pointer()[i]) for i in range(self.num_sym)]
        heapq.heapify(self.h)
        for i in range(self.num_sym - 1):
            first_small = heapq.heappop(self.h)
            second_small = heapq.heappop(self.h)
            merged = self.merge(first_small, second_small)  # merge the as leaves
            heapq.heappush(self.h,merged)
        self.tree.root = heapq.heappop(self.h)[1]

    def merge(self, first_small, second_small):
        merged_weight = first_small[0] + second_small[0]
        merged_leaf = leaves('(' + first_small[1].name + '_' + second_small[1].name + ')',
                             min(first_small[1].rank, second_small[1].rank) + 1)
                            # min for the minimum lenghth, max for the maximun length!
        first_small[1].parent = merged_leaf.name
        second_small[1].parent = merged_leaf.name
        return (merged_weight, merged_leaf)

run = huffman('huffman.txt')
run.read_file()
run.build_tree()
print(run.tree.root.rank)