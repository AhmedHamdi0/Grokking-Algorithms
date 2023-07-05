def find_smallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[smallest_index]
    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr
