def insertion_sort(li):
    n = len(li)
    for i in range(1, n):  # Start from the second element (index 1)
        key = li[i]  # Current element to be inserted
        j = i - 1  
        
        # Move elements of li[0..i-1], that are greater than key, one position ahead
        while j >= 0 and li[j] > key:
            li[j + 1] = li[j]
            j -= 1
        
        li[j + 1] = key  # Insert key at its correct position

    return li

# Example usage
li = [4, 3, 5, 1, 2, 6]
print(insertion_sort(li))
