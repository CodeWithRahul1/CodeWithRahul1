
# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):

    if (r >= l):

        # Find the mid1 and mid2
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3

        # Check if key is present at any mid
        if (ar[mid1] == key): 
            return mid1
        
        if (ar[mid2] == key): 
            return mid2
        
        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        if (key < ar[mid1]): 

            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar)
        
        elif (key > ar[mid2]): 

            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar)
        
        else: 

            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1, 
                                 mid2 - 1, key, ar)
        
    # Key not found
    return -1

# Driver code
l, r, p = 0, 9, 5
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Starting index
l = 0
# end element index
r = 9
# Key to be searched in the array
key = 5
# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)


"""
What is the Ternary Search?
    Ternary search is a search algorithm that is used to find the position of a target value within a sorted array. It operates on the principle of dividing the array into three parts instead of two, as in binary search. The basic idea is to narrow down the search space by comparing the target value with elements at two points that divide the array into three equal parts.

    mid1 = l + (r-l)/3 
    mid2 = r - (r-l)/3 

When to use Ternary Search:
    When you have a large ordered array or list and need to find the position of a specific value.
    When you need to find the maximum or minimum value of a function.
    When you need to find bitonic point in a bitonic sequence.
    When you have to evaluate a quadratic expression

Working of Ternary Search:
    The concept involves dividing the array into three equal segments and determining in which segment the key element is located. It works similarly to a binary search, with the distinction of reducing time complexity by dividing the array into three parts instead of two.

Below are the step-by-step explanation of working of Ternary Search:

Initialization:
    Set two pointers, left and right, initially pointing to the first and last elements of our search space.

Divide the search space:
    Calculate two midpoints, mid1 and mid2, dividing the current search space into three roughly equal parts:
    mid1 = left + (right - left) / 3
    mid2 = right - (right - left) / 3
    The array is now effectively divided into [left, mid1], (mid1, mid2), and [mid2, right].
Comparison with Target:.
    If the target is equal to the element at mid1 or mid2, the search is successful, and the index is returned
    If the target is less than the element at mid1, update the right pointer to mid1 - 1.
    If the target is greater than the element at mid2, update the left pointer to mid2 + 1.
    If the target is between the elements at mid1 and mid2, update the left pointer to mid1 + 1 and the right pointer to mid2 - 1.
Repeat or Conclude:
    Repeat the process with the reduced search space until the target is found or the search space becomes empty.
    If the search space is empty and the target is not found, return a value indicating that the target is not present in the array.

"""