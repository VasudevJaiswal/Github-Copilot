# Finding the smallest five elements in an array sorted in ascending order.

def smallest_five(arr):
    arr.sort()
    return arr[:5]