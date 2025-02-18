

def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

"""
1. What is linear search algorithm?
Linear search algorithm, also known as sequential search algorithm, is a simple searching algorithm that traverses a list or array sequentially to find a target element. In Linear Search, we can get the 


2. How does linear search algorithm work?
Linear search algorithm iterates through each element in the list or array, comparing it with the target element until a match is found or the end of the list is reached. If the end of the list is reached, then it means that the target element is not present in the array.


3. What is the time complexity of linear search algorithm?
The time complexity of linear search algorithm is O(n), where n is the number of elements in the list or array being searched. This means the time taken for searching increases linearly with the size of the input.


4. When is linear search algorithm preferred over other searching algorithms?
Linear search algorithm is preferred when the list or array is unsorted, or when the size of the input is relatively small. It’s simple to implement and doesn’t require the data to be in any specific order.

"""