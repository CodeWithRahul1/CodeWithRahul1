def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water

def trap1(height):
    max_hight = min(height[0], height[-1])
    print(max_hight)
    water = 0
    for i in range(1,len(arr)-1):
        cuurent_level = max_hight - height[i]
        water += cuurent_level
    return water


# Example usage
arr = [4, 2, 0, 3, 2, 5]
# print(trap(arr))
print(trap1(arr))  # Output: 9