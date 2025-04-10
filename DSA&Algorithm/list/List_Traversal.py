'''
You are given a list that contains integers. You need to print the elements of the list with a space between them.
Note: Do not add a new line at the end.

Examples:

Input: arr = [54, 43, 2, 1, 5]
Output: 54 43 2 1 5
Explanation: Just traverse and print the numbers.
'''

def ListTraversal(li):
    res = ''
    for i in li:
        print(i , end=' ')


li = [54, 43, 2, 1, 5]
ListTraversal(li)