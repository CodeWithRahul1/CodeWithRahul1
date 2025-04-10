'''You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

Examples:

Input: arr = [54, 43, 2, 1, 5]
Output: 53 42 1 0 5
Explanation: Just decrement the numbers by 1.'''

def DecerementValue(arr):
    res = list(map(lambda x:x-1, arr))
    return res


arr = [54, 43, 2, 1, 5]
print(DecerementValue(arr))