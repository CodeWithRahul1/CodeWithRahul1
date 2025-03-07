def method(arr, target):
    left = 0
    current_sum = 0
    for right in range(len(arr)):
        current_sum +=arr[right]  
        while current_sum> target:
            current_sum -= arr[left]
            left +=  1
        if current_sum == target:
            return arr[left:right+1]
    return -1
        




arr = [2,4,6,7,8,9,10,11]
target = 24
print(method(arr, target))