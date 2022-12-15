opponent = []
response = []

with open('day2.txt', 'r') as f:
    for line in f:
        opponent.append(line.strip()[0])
        response.append(line.strip()[2])

t = list(zip(opponent, response))

# part 1
outcome = {
    'X': {'val': 1, 'A': 3, 'B': 0, 'C': 6},
    'Y': {'val': 2, 'A': 6, 'B': 3, 'C': 0},
    'Z': {'val': 3, 'A': 0, 'B': 6, 'C': 3}
}

s = 0
for o, r in t:
    s += outcome[r]['val'] + outcome[r][o]

print(s)

# part 2
new_outcome = {
    'X': {'status': 0, 'A': 3, 'B': 1, 'C': 2},
    'Y': {'status': 3, 'A': 1, 'B': 2, 'C': 3},
    'Z': {'status': 6, 'A': 2, 'B': 3, 'C': 1}
}

s = 0
for o, r in t:
    s += new_outcome[r]['status'] + new_outcome[r][o]

print(s)