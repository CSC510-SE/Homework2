"""
This module contains an implementation of the Merge Sort algorithm in Python, which is a
divide-and-conquer sorting algorithm.
"""

import rand

def merge_sort(input_arr):   # renamed 'arr' to 'input_arr'
    """
    Recursively splits the input array into halves and sorts them using merge sort.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: A sorted version of the input array.
    """
    # Ensure there are no None values in the array
    input_arr = [x for x in input_arr if x is not None]

    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The first sorted array.
        right_arr (list): The second sorted array.

    Returns:
        list: A merged and sorted array combining left_arr and right_arr.
    """
    merge_arr = []
    left_index = 0
    right_index = 0

    # Merge the two arrays
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Append any remaining elements in left_arr or right_arr
    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


# Generating an array with random integers (removing None)
arr = [x for x in rand.random_array([None] * 20) if x is not None]

# Sorting the array
arr_out = merge_sort(arr)

print(arr_out)
