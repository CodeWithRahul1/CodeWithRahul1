def Method(arr, k):
    
    min_max_arr = []
    for i in range(len(arr)-k+1):
        min_value = min(arr[i:k+i])
        max_value = max(arr[i:k+i])
        addition_of_min_max = min_value + max_value
        min_max_arr.append(addition_of_min_max)
    return sum(min_max_arr)
    
    


arr= [2, 5, -1, 7, -3, -1, -2]
k = 4


print(Method(arr, k))