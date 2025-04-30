def method(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n %2 ==0:
        print(n//2)
        print(n%2)
        print(nums1[n // 2 - 1])
        print(nums1[n // 2])

        median = (nums1[n // 2 - 1] + nums1[n // 2]) / 2
        return median
        
    else:
        median = nums1[n // 2]
        return median
    
        



nums1 = [1,2]
nums2 = [3,4]
print(method(nums1, nums2))
