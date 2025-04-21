'''
Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation: First window is [1, 2, 1, 3], count of distinct numbers is 3.
                      Second window is [2, 1, 3, 4] count of distinct numbers is 4.
                      Third window is [1, 3, 4, 2] count of distinct numbers is 4.
                      Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.


Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: First window is [4, 1], count of distinct numbers is 2.
                      Second window is [1, 1], count of distinct numbers is 1.
'''
def distinct_numbers(arr, k):
    distinct_list = []
    for i in range(0, len(arr)-k+1):
        new_list = arr[i:i+k]
        distinct_value = len(set(new_list))
        distinct_list.append(distinct_value)
        
    return distinct_list



arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(distinct_numbers(arr, k))