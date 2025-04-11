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


def move_zeros_in_place(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            nums.pop(i)
            nums.append(0)
            
    return nums
            


nums = [0,1, 0, 5, 0, 3, 4, 6, 0,7,0,]
move_zeros_in_place(nums)
print(nums)