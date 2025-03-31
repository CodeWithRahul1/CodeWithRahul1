def superReducedString(s):
    # Write your code here
    stack = []
    for char in s:
        
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack) if stack else 'Empty String'
s = 'aaabccddd'
print(superReducedString(s))