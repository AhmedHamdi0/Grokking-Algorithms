# Write a recursive function to sum an array applying divide & conquer
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


# Write a recursive function to count the number of items in a list
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


# Write a recursive function to get the max item in a list
def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_arr = max(arr[1:])
    return arr[0] if arr[0] > sub_arr else sub_arr


# Quicksort algorithm implementation
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]      # random pivot is much better
        less_arr = [i for i in arr[1:] if i <= pivot]
        greater_arr = [i for i in arr[1:] if i > pivot]
        return quicksort(less_arr) + [pivot] + quicksort(greater_arr)