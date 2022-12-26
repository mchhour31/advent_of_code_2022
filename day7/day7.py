filename = 'day7_test.txt'

c = 0
cd_list = []
t_files = []

test = []

size_files = []
with open(filename) as f:
    for line in f:
        if 'cd' in line:
            cd_list.append(line.split('\n')[0].split('$')[-1].split()[-1])
        
        if 'cd' not in line:
           t_files.append(line.split('\n')[0])
    
    a = [[] for _ in range(t_files.count('$ ls'))] # list of empty lists
    
    for n in t_files:
        test.append(n.split('$ ls')[-1])
    
    x = 0
    test = test[1:]
    
    print(test)
    for i in range(len(test)):
        if test[i] == '':
            x += 1
            continue # skip when ''

        a[x].append(test[i])
    
    cd_list = [x for x in cd_list if x != '..']
    
    sls = []
    s = 0
    
    a_tmp = [[] for _ in range(len(a))]
    
    for i, n in enumerate(a):
        for j in n:
            if j.split()[0] == 'dir':
                a_tmp[i].append(j.split()[1]) # tracking directories with subdirectories

            if j.split()[0] != 'dir':
                s += int(j.split()[0]) # calculates size of each directory
            
        sls.append(s)
        s = 0 # resets sum for each directory
            
    print(sls)
    print(cd_list)
    print(a_tmp)
    
    # for i, dir in enumerate(a_tmp):
    #     for j in dir:
    #         # print(a_tmp)
    #         print(a_tmp[cd_list.index(j)])
            # for x in a_tmp[cd_list.index(j)]:
            #     # sls[i] += sls[cd_list.index(x)]
            #     print(sls)            
            # sls[i] += sls[cd_list.index(j)]
                
            # print(sls[cd_list.index(j)])
            # print(j)
            
            # print(sls[i])
            
            # print(cd_list.index(j))
            
            
            # print(sls[cd_list.index(j)])
            
    #         # print(j, cd_list.index(j))
    print(sls) 
    
    filter_ls = list(filter(lambda x: x < 100000, sls))
    
    print(sum(filter_ls))
        
        
        # sls[0] = sum(sls)
        
        # print(sls)

            
        # if 'dir' not in j.split():
            #     size_files.append(j.split()[0])
                
            # print(j.split())
        
    
    
    # # print(cd_list)
    # # print(a)
    
    
    # # print(cd_list)
    # # print(test)