#remove duplicate element from list
l = [11, 21, 21, 13, 41, 41, 5]

n = []

for item in l:
    if item not in n:
        n.append(item)

print("List after removing duplicates:", n)
