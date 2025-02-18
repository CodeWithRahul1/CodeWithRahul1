#Defination is below of the code

# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")





"""
What is Binary Search Algorithm?
Binary search is a search algorithm used to find the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty. The search interval is halved by comparing the target element with the middle value of the search space.

Conditions to apply Binary Search Algorithm in a Data Structure
To apply Binary Search algorithm:
    The data structure must be sorted.
    Access to any element of the data structure should take constant time.

Binary Search Algorithm

    Divide the search space into two halves by finding the middle index “mid”. 
    Compare the middle element of the search space with the key. 
    If the key is found at middle element, the process is terminated.
    If the key is not found at middle element, choose which half will be used as the next search space.
        If the key is smaller than the middle element, then the left side is used for next search.
        If the key is larger than the middle element, then the right side is used for next search.
    This process is continued until the key is found or the total search space is exhausted.
"""