'''Two-Pointer Technique – O(n) time and O(1) space
The idea of this technique is to begin with two corners of the given array. We use two index variables left and right to traverse from both corners.

Initialize: left = 0, right = n – 1
Run a loop while left < right, do the following inside the loop

Compute current sum, sum = arr[left] + arr[right]
If the sum equals the target, we’ve found the pair.
If the sum is less than the target, move the left pointer to the right to increase the sum.


If the sum is greater than the target, move the right pointer to the left to decrease the sum.'''
def method(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return sum == target
        
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False




arr = [0, -1, 2, -3, 1]
target = -2

print(method(arr, target))