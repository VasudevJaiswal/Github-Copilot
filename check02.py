# Find the index of the last occurrence of a number in a list.

def last_index(lst, number):
    """
    Return the index of the last occurrence of a number in a list.
    """
    if lst == []:
        return -1
    else:
        return lst.index(number)