import string as st

lower_priori = dict(zip(list(st.ascii_lowercase), list(range(1, 27))))
upper_priori = dict(zip(list(st.ascii_uppercase), list(range(27, 53))))

s = 0 
with open('day3.txt', 'r') as f:
    for l in f:
        x = l.strip()

        x1, x2 = x[:(len(x) // 2)], x[(len(x) // 2):]
        
        character = list(set(x1).intersection(x2))[0]
        
        if character.isupper():
            s += upper_priori[character]
        else:
            s += lower_priori[character]
        

# print(x)
# print(x1, x2)

# print(list(set(x1).intersection(x2))[0])

print(s)