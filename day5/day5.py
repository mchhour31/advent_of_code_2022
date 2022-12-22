def splitString(line, seps):
    ls = []
    
    s = line
   
    s = s.replace('move', ',').split(',')
    s = s[1].replace('from', ',').split(',')
    ls.append(int(s[0]))
    
    s = s[1].replace('to', ',').split(',')
    ls.append(int(s[0]))
    
    s = s[1].split('\n')
    ls.append(int(s[0]))

    return ls

def flatten(l):
    return [item for sublist in l for item in sublist]

r = -1
with open('day5_input.txt', 'r') as f:
    all = []
    for line in f:
        all.append(line) # appending all lines into a list
    
    for z in all:
        if '1' in z and 'move' not in z:
            stack_idx = all[all.index(z)] # selecting the line w stack index numbers
            stack_elements = all[:all.index(z)] # selects the stack elements
            movements = all[all.index(z)+2:] # selects the instructions section
            
    stack_of_words = [[] for _ in range(len(stack_idx.split()))] # array of lists of size = number of stacks

    # appending stack elements to an array 
    for k in range(len(stack_elements)):
        for i in range(len(stack_idx.split())):
            stack_of_words[i].append(stack_elements[k].split('\n')[0][i*4:i*4+3])

    # removing white spaces, stack will be treated as left = top of stack
    for ls in stack_of_words:	
        while ('   ' in ls):
            ls.remove('   ')
        
    print(stack_of_words)
    
    # process the instructions to isolate integers ie. [num_selected, origin, destination]
    for i in movements:
        movements = splitString(i, ['move', 'from', 'to', '\n'])
        
        start = stack_of_words[movements[1]-1]
        end = stack_of_words[movements[2]-1]
        
        if movements[0] == 1:
            for i in range(movements[0]):
                end.insert(0, start[0]) # adding to the lhs of end array
                start.remove(start[0]) # removing from the start array
        else:
            end.insert(0, start[:movements[0]]) # adding to the lhs of end array
            end = flatten(end)
            # start = list(set(start) - set(start[:movements[0]]))
            print(end)
    
    # joining every top element for every stack
    final = ""
    for top in stack_of_words:
        final += top[0]
    
    print(final)

            



