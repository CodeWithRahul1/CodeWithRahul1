''' You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list.

Examples:

Input: a = 1, b = 2, c = 3
Output: 1 2 3
Explanation: Just create a list and append 1 2 3 to it. Then return [1,2,3] list.'''


def AppendToList(a, b , c):
     res = []
     res.append(a)
     res.append(b)
     res.append(c)
     return res

a = 1
b = 2
c = 3

print(AppendToList(a, b , c))
