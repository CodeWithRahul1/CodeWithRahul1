def method():
    left = 0
    current_sum = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        while left < right and current_sum >target:
            current_sum = current_sum - nums[left]
            left -= 1

        if current_sum == target:
            return nums[left: right+1]
        
        