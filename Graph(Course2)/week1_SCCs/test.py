def Graph_read(file_name):
    G = {}
    G_rev = {}
    with open(file_name) as f:
        count =0
        handle = open('SCC_test.txt','w')
        for line in f:
            handle.write(line)
            count = count + 1
            if count > 1000:
                break
Graph_read('SCC.txt')
