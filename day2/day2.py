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


# total_1 = 0
# total_2 = 0
# selected_1 = 0
# selected_2 = 0
# outcome_1 = 0
# outcome_2 = 0

# # # part1 - naive approach
# for a, x in t:
#     if a == 'A' and x == 'Z':
#         selected_1, selected_2 = 1, 3
#         outcome_1, outcome_2 = 6, 0
#     elif a == 'A' and x == 'Y':
#         selected_1, selected_2 = 1, 2
#         outcome_1, outcome_2 = 0, 6
#     elif a == 'A' and x == 'X':
#         selected_1, selected_2 = 1, 1
#         outcome_1, outcome_2 = 3, 3
    
#     if a == "B" and x == 'Z':
#         selected_1, selected_2 = 2, 3
#         outcome_1, outcome_2 = 0, 6
#     elif a == "B" and x == 'Y':
#         selected_1, selected_2 = 2, 2
#         outcome_1, outcome_2 = 3, 3
#     elif a == "B" and x == 'X':
#         selected_1, selected_2 = 2, 1
#         outcome_1, outcome_2 = 6, 0
        
#     if a == 'C' and x == 'Z':
#         selected_1, selected_2 = 3, 3
#         outcome_1, outcome_2 = 3, 3
#     elif a == 'C' and x == 'Y':
#         selected_1, selected_2 = 3, 2
#         outcome_1, outcome_2 = 6, 0
#     elif a == 'C' and x == 'X':
#         selected_1, selected_2 = 3, 1
#         outcome_1, outcome_2 = 0, 6
    
#     total_1 += selected_1 + outcome_1
#     total_2 += selected_2 + outcome_2

# print(total_1, total_2)

# # part2
# d = {'X': 0, 'Y': 3, 'Z': 6}

# s = 0

# for a, x in t:
#     if a == 'A':
#         if d[x] == 0:
#             z = 3
#         elif d[x] == 3:
#             z = 1
#         elif d[x] == 6:
#             z = 2
            
#     elif a == 'B':
#         if d[x] == 0:
#             z = 1
#         elif d[x] == 3:
#             z = 2
#         elif d[x] == 6:
#             z = 3
    
#     elif a == 'C':
#         if d[x] == 0:
#             z = 2
#         elif d[x] == 3:
#             z = 3
#         elif d[x] == 6:
#             z = 1
    
#     s += d[x] + z

# print(s)