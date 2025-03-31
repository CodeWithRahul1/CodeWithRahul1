s = "geeksforgeeks"

# Check if the `s` contains at least one letter
l= any(c.isalpha() for c in s)

# Check if the `s` contains at least one number
n= any(c.isdigit() for c in s)

# If both conditions are met
if l and n:
    print(True) 
else:
    print(False)
import re
s = "Python123"

# checks for lettors
l = bool(re.search(r'[a-zA-Z]', s))  
# checks for digits 
n = bool(re.search(r'\d', s))  

if l and n:
    print(True)
else:
    print(False)
