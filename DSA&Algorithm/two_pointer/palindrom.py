def is_palindrome(string):
    left= 0
    right = len(string)-1
    while left < right:
        print(string[left], string[right])
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return  True
    
li = [1,2,4,5,2,1]
print(is_palindrome(li))  