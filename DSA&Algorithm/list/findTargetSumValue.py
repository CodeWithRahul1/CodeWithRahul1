def find_two_sum(nums, target):
    seen = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        print(diff)
        if diff in seen:
            return diff, nums[i]
        seen[nums[i]] = i
    return None

# Example
nums = [2, 7, 11, 15]
target = 13
result = find_two_sum(nums, target)
print(result)  # Output: (2, 7)