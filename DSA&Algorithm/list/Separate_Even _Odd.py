'''You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers.

Examples:

Input: arr = [54, 43, 2, 5, 14, 17, 18, 9]
Output: even: 54 2 14 18, odd: 43 5 17 19'''

def Method(arr):
    even = list(filter(lambda x:x % 2 == 0, arr))
    odd = list(filter(lambda x: x % 2 != 0, arr))
    return even, odd


arr = [54, 43, 2, 5, 14, 17, 18, 9]
print(Method(arr))