import string as st

lower_priori = dict(zip(list(st.ascii_lowercase), list(range(1, 27))))
upper_priori = dict(zip(list(st.ascii_uppercase), list(range(27, 53))))

s = 0 
with open('day3.txt', 'r') as f:
    lines = f.read().split('\n')

x = []
# filtering out groups in lines of 3
for i in range(0, len(lines), 3):
    groups = lines[i:i+3]

    # iterating through groups finding unique characters, appending to list
    for j in range(1, len(groups)):
        curr = list(set(groups[j-1]).intersection(groups[j]))
        
        x.append(curr)

# iterating through unique characters, finding common unique chars
for k in range(0, len(x), 2):
    character = list(set(x[k]).intersection(x[k+1]))[0]
    
    if character.isupper():
        s += upper_priori[character]
    else:
        s += lower_priori[character]

print(s)