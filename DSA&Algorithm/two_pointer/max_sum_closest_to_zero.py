# def max_sum_closest_to_zero(arr):
#     arr.sort()
#     left, right = 0, len(arr) - 1
#     closest_sum = float('inf')  
#     max_sum = float('-inf')
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if abs(current_sum) < abs(closest_sum):
#             closest_sum = current_sum
#             max_sum = current_sum
#         elif abs(current_sum) == abs(closest_sum):
#             max_sum = max(max_sum, current_sum)  # choose max one

#         # Move pointers
#         if current_sum < 0:
#             left += 1
#         else:
#             right -= 1

#     return max_sum

# arr = [1, 60, -10, 70, -80, 85]
# print(max_sum_closest_to_zero(arr))


def max_sum_closest_to_zero(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
        elif abs(current_sum) == abs(closest_sum):
            closest_sum = max(closest_sum, current_sum)

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_sum
arr = [1, 60, -10, 70, -80, 85]
print(max_sum_closest_to_zero(arr))
# result = max_sum_closest_to_zero(arr)
# print("Max sum closest to zero:", result)

'''
1. sort the arry

2. intitalize the left right pointer
    left = 0 
    right = len(arr)-1

3. Intialize the tracking variable

    closest_sum = float(int)
    max_sum = float(-n)

4. loop while left < right

5. calulate the current_sum
    current_sum = arr[left] + arr[right]

6. check if abs(current_sum) < closest_sum:
    closet_sum = current_sum
    max_sum = current_sum
7. elif abs(current_sum) == abs(closest_sum):
    max_sum = max(abs(current_sum), abs(closet_sum)

8. if current_sum < 0:
    left += 1
9. else:
    right -= 1

10. 
    returh max_sum






'''
