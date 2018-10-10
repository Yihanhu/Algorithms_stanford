def readfile(filename):
    with open(filename, 'r') as f:
        i = 0
        vertices = []
        for line in f:
            i = i + 1
            if i == 1:
                v_num = int(line.split()[0])
                bit_num = int(line.split()[1])
                continue
            vertices.append("".join(line.split()))
    return v_num, bit_num, vertices

def readfile_small(filename):
    with open(filename, 'r') as f:
        i = 0
        vertices = []
        for line in f:
            i = i + 1
            if i == 1:
                v_num = int(line.split()[0])
                bit_num = int(line.split()[1])
                continue
            vertices.append("".join(line.split()))
            if i == 30000:
                break
    return 30000, bit_num, vertices


def inverse(bit):
    return str(int(bit == '0'))


def similar(v):
    out = [v]
    for i in range(len(v)):
        out.append(v[:i] + inverse(v[i]) + v[i + 1:])
        for j in range(i + 1, len(v)):
            out.append(v[:i] + inverse(v[i]) + v[i + 1:j] + inverse(j) + v[j + 1:])
    return out


v_num, bit_num, vertices = readfile('clustering_big.txt')
# v_num, bit_num, vertices = readfile_small('clustering_big.txt')
print('intial:',len(vertices))
heads = {}
ranks = {}
for v in vertices:
    heads[v] = v
    ranks[v] = 0
# print(len(head.keys()))
num_clus = len(heads.keys())# remaining unidentical clusterings
for v in vertices:          # v in vertices can only be pointed at, because it is new
    for friend in similar(v):
        if heads.get(friend) != None:
            head = heads[friend]
            while heads[head] != head:
                head = heads[head]
            v_head = heads[v]
            while heads[v_head] !=v_head:
                v_head = heads[v_head]
            if head != v_head:
                # heads[v_head] = head
                if ranks[v_head] == ranks[head]:
                    heads[v_head] = head
                    ranks[head] = ranks[head] + 1
                elif ranks[v_head] > ranks[head]:
                    heads[head] = v_head
                else:
                    heads[v_head] = head
                num_clus -= 1
            print(num_clus)

# print(num_clus)


#
