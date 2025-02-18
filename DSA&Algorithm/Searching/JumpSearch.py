import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Block size
    prev = 0

    # Jumping ahead in steps until we find the range
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Target not found

    # Performing linear search within the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  # Return the index if found

    return -1  # Element not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 15
result = jump_search(arr, target)

print("Element found at index:", result if result != -1 else "Not found")
