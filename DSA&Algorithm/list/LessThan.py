'''You are given a number k and a list arr that contains integers. You need to return list of numbers that are less than k.

Examples:

Input: arr = [54, 43, 2, 1, 5], k = 6
Output: 2 1 5
Explanation: 2 1 5 are less than 6.'''


def LessThan(arr, k):
    res = list(filter(lambda x: x < k , arr ))
    return res


arr = [54, 43, 2, 1, 5]
k = 6
print(LessThan(arr, k))
