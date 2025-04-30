def method(string):
        mapping = {'}':'{', ')':'(', ']':'['}
        stack = []
        for char in string:
            if char in mapping.values():
                stack.append(char)
            
            elif stack and stack[-1] ==mapping[char]:
                    stack.pop(-1)
            else:
                return False
        return len(stack)==0
                    

string = ']'
print(len(string))
print(method(string))