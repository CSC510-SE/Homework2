import pytest
from hw2_debugging import merge_sort

def test_merge_sort_empty():
    """Test sorting an empty array."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting an array with a single element."""
    assert merge_sort([1]) == [1]

def test_merge_sort_sorted():
    """Test sorting an already sorted array."""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test sorting a reverse sorted array."""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    """Test sorting an unsorted array."""
    assert merge_sort([3, 1, 4, 5, 2]) == [1, 2, 3, 4, 5]

def test_merge_sort_with_duplicates():
    """Test sorting an array with duplicate elements."""
    assert merge_sort([3, 1, 2, 1, 5, 2]) == [1, 1, 2, 2, 3, 5]

def test_merge_sort_large_random():
    """Test sorting a large randomly shuffled array."""
    arr = [20, 10, 15, 1, 25, 5, 17, 30]
    assert merge_sort(arr) == [1, 5, 10, 15, 17, 20, 25, 30]

# These are the Example of edge cases with the negetive Integers
def test_merge_sort_with_negative_numbers():
    """Test sorting an array with negative numbers."""
    arr = [3, -1, 4, -5, 2]
    assert merge_sort(arr) == [-5, -1, 2, 3, 4]

