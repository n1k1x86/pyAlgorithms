from typing import Sequence

def binarySearch(arr: Sequence[int], elem) -> int:
    """Function that search your element via binary search algorithm
    Note: entering sequence must be sorted
    Return: element that function searched or None if function couldn't find it"""
    min_ind = 0
    max_ind = len(arr) - 1

    while min_ind <= max_ind:
        mid = round((max_ind + min_ind) / 2)
        guess_elem = arr[mid]
        print(f'{guess_elem} index is {mid}')
        if guess_elem == elem:
            return f"{guess_elem} index is {mid}"
        elif guess_elem > elem:
            max_ind = mid - 1
        elif guess_elem < elem:
            min_ind = mid + 1

    return None
