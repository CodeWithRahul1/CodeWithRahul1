def permutation(lst): 
    
    if len(lst) == 0:
        return [] 
    
    if len(lst) == 1:
        return [lst]
    
 
    l = []
   
    for i in range(len(lst)):
       m = lst[i]       
       remLst = lst[:i] + lst[i+1:]
       print(remLst)
       for p in permutation(remLst):
           l.append([m] + p)           
    return l

data = [1,2,3]
print(permutation(data))






def permute_in_place(arr, start=0, res=None):
    if res is None:
        res = []
    
    if start == len(arr) - 1:
        res.append(arr[:])  # append a copy of current permutation
        return res
    
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]  # swap
        permute_in_place(arr, start + 1, res)
        arr[start], arr[i] = arr[i], arr[start]  # swap back (backtrack)
    
    return res[1]

arr = [1, 2, 3]
permutations = permute_in_place(arr)
print(permutations)