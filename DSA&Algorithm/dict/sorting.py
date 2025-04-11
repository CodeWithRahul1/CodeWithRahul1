
di = {'a': 2, 'c': 1, 'b': 3}

# Step 1: Convert dictionary to a list of tuples
items = list(di.items())

# Step 2: Manually sort the list of tuples based on values
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] > items[j + 1][1]:
            # Swap
            items[j], items[j + 1] = items[j + 1], items[j]

# Step 3: Reconstruct dictionary
sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value

print(sorted_dict)
