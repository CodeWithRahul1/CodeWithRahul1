def TwoSum(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        if sum < target:
            left += 1
        else:
            right -= 1
    return -1

arr = [0, -1, 2, -3, 1]
target = -2

print(TwoSum(arr, target))
