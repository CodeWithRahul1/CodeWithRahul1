def move_zeros_in_place(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos +=1
    

    while pos < len(nums):
        nums[pos] = 0
        pos += 1
    return nums


nums = [1, 0, 2, 0, 3, 4]
move_zeros_in_place(nums)
print(nums)

### second approch


def move_zeros_and_sort(nums):
    # Step 1: Count non-zero elements and collect them
    non_zeros = []
    for i in range(len(nums)):
        if nums[i] != 0:
            non_zeros.append(nums[i])

    # Step 2: Sort non-zero elements using simple bubble sort
    for i in range(len(non_zeros)):
        for j in range(i + 1, len(non_zeros)):
            if non_zeros[i] > non_zeros[j]:
                non_zeros[i], non_zeros[j] = non_zeros[j], non_zeros[i]

    # Step 3: Put sorted non-zeros back and fill remaining with zeros
    for i in range(len(non_zeros)):
        nums[i] = non_zeros[i]
    
    for i in range(len(non_zeros), len(nums)):
        nums[i] = 0

    return nums

# Example
nums = [1, 0, 5, 0, 3, 4]
move_zeros_and_sort(nums)
print(nums)  # Output: [1, 3, 4, 5, 0, 0]