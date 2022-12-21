def splitString(line, seps):
    ls = []
    
    s = line
    
    # seperating string at [move, from, to], and appending the numbers to new list
    for sep in seps:
        s = s.split(sep)[1] 
        ls.append(int(s[1]))
        
        print(s)
        
    return ls

with open('day5_input.txt', 'r') as f:
    x = []
    t = []
    s1, s2, s3 = [], [], []
    
    for line in f:
        t.append(line)
        
        if '[' in line:
            x.append(line) 
    
    print(t[9:])
    
    # # seperating string into indiviudal lists
    # for i in x:
    #     s1.append(i.split('\n')[0][:3])
    #     s2.append(i.split('\n')[0][4:7])
    #     s3.append(i.split('\n')[0][8:11])
        
    # s = [' '.join(s1).split(), ' '.join(s2).split(), ' '.join(s3).split()] # removing empty strings on lhs of characters
    # # s = [s1, s2, s3]
    
    # # print(s)
    # a = ""
    
    # for z in t[5:]:
    #     ori_dest = splitString(z, ['move', 'from', 'to']) # list of [item, origin, destination] indexes
    #     start = s[ori_dest[1]-1]
    #     end = s[ori_dest[2]-1]
        
    #     print(ori_dest)
    #     # while ('   ' in end):
    #     #     end.remove('   ')
        
    #     # while ('   ' in start):
    #     #     start.remove('   ')
        
        
    #     for num_move in range(ori_dest[0]):
    #         end.insert(0, start[0])    
    #         start.remove(start[0])
            
    #         # print(start, end)
                
    #     # print(s)
        
                
    #     #     
            
    #     #     print(end)
        
    #     # print(s)
            

            



