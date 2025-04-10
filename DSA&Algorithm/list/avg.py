'''You are given a list arr that contains integers. You need to return average of the non negative integers.

Examples:

Input: arr = [-12, 8, -7, 6, 12, -9, 14]
Output: avg = 10.0
Explanation: The non negative numbers are 8 6 12 14. The sum is 8+6+12+14 = 40, Average = 40/4 = 10.0'''

def Average(arr):
    su = list(filter(lambda x:x >=0, arr))
    count = 0
    sum = 0
    for num in su:
        count += 1
        sum += num

    return sum/count




arr = [-12, 8, -7, 6, 12, -9, 14]
print(Average(arr))
