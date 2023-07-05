def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:
        middle = (low + high) /2
        guess = list[middle]

        if guess == item:
            return middle
        elif guess > item:
            high = middle - 1
        else:
            low = middle + 1
        return None
