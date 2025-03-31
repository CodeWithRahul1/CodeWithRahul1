s = "GeeksforGeeks"
new_dic = {}

# Count character frequencies
for char in s:
    if char in new_dic:
        new_dic[char] += 1
    else:
        new_dic[char] = 1

# Convert dictionary to list of tuples (char, frequency)
items = [(key, value) for key, value in new_dic.items()]
pn = len(items)  # Correct length of items list

# Implement Selection Sort on (key, value) pairs based on values
for i in range(pn):
    min_index = i
    for j in range(i + 1, pn):
        if items[j][1] < items[min_index][1]:  # Comparing values
            min_index = j
    # Swap the found minimum element with the first element
    items[i], items[min_index] = items[min_index], items[i]

# Convert sorted list back to a dictionary
sorted_dict = {key: value for key, value in items}

print(sorted_dict)
