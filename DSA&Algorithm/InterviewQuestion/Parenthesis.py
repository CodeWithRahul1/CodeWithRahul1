def method(st):
     mapping_key  = {'}':'{', ')':'(', ']':'['}
     stack = []
     for char in st:
          if char in  mapping_key.values():
               stack.append(char)
          elif char in mapping_key:
               stack.pop(-1)
          else:
               return -1
     return len(stack) == 0



st = '{([[]!])}'
print(method(st))