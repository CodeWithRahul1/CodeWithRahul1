def selection_sort(li):
    n = len(li)
    for i in range(n):
        min_index = i  
        for j in range(i + 1, n):
            if li[j] < li[min_index]:
                min_index = j 
        li[i], li[min_index] = li[min_index], li[i] 
    return li

# Example usage
li = [4, 3, 5, 1, 2, 6]
print(selection_sort(li))
