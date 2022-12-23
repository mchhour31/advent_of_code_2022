def detect_duplicates(s:str) -> bool:
    for i in s:
        if s.count(i) > 1:
            return True
    
    return False

with open('day6_input.txt') as f:
    for line in f:
        string = line
        
    n = 14
    chunks = [string[i:i+n] for i in range(0, len(string))] # list of all possible size 4 chunks
    
    for i, n in enumerate(chunks):
        if detect_duplicates(n) == False:
            x = i
            break

    part_one = string.find(chunks[x])+4 # change n = 4
    part_two = string.find(chunks[x])+14
    
    print(part_two)
    
    