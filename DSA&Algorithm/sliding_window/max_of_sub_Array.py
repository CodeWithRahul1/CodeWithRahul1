def maximumSumSubarray(arr,k):
        if len(arr)<k:
            return 'Invalid Input'
        print(arr[:k])
        max_sum= sum(arr[:k])
        res = max_sum
        for i in range(k, len(arr)):
            max_sum += arr[i] - arr[i-k]
            if res < max_sum:
                res = max_sum
        return res
            # print(new_sum)
            
        

arr = [100, 200, 300, 400]
k = 1

print(maximumSumSubarray(arr,k))