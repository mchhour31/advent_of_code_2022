t = 0
c = 0
with open('day4_input.txt', 'r') as f:
    for line in f:
        x = line.strip().split(',')
        t = [y.split('-') for y in x]

        f, s = t[0], t[1] # seperating out sublists
        
        ls_f = [int(f[i]) for i in range(len(f))] # converting sublist elements to type int
        ls_s = [int(s[i]) for i in range(len(s))] # converting sublist elements to type int
        
        z0 = [a for a in range(ls_f[0], ls_f[1]+1)] # generating lists from range t0 to t1
        z1 = [a for a in range(ls_s[0], ls_s[1]+1)]
        
        # if ((set(z0) & set(z1)) == set(z1)) or ((set(z0) & set(z1)) == set(z0)):
        #     c += 1
        
        if (set(z0) & set(z1)):
            c += 1

    print(c)
    
    
        # for a in range(ls_f[0], ls_f[1]):
        #     print([a])

        # print(z)