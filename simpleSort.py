from typing import List

def find_min_elem(arr: List):
    """Function that finds a min element in array"""
    min_elem = arr[0]
    min_elem_ind = 0
    for i in range(len(arr)):
        if min_elem > arr[i]:
            min_elem = arr[i]
            min_elem_ind = i
    return min_elem_ind

def simple_sort(arr: List):
    """Function that reliazes a simple sort"""
    sorted_arr = []
    for i in range(len(arr)):
        smallest_elem = find_min_elem(arr)
        sorted_arr.append(arr.pop(smallest_elem))
    return sorted_arr
