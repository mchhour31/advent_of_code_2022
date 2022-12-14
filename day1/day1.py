#### PART 1
# reading input file
with open('day1.txt', 'r') as f:
    x = [line.strip() for line in f]

# seperating into sublists at all cases of ""
ls = [[]]
for l in x:
    if l == '':
       ls.append([]) 
    else:
        ls[-1].append(l)

# converting list elements to integer type
numbers = [list(map(int, x)) for x in ls]

t = []
# finding maximum 
for i in numbers:
    t.append(sum(i))

print(max(t))

#### PART 2
# finding top 3 elves (ie. 3 largest vals)
s = 0
for _ in range(3):
    curr_max = max(t)
    s += curr_max
    t.remove(curr_max)
    
print(s)