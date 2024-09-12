"""
This module generates a random array with numbers between 1 and 20.
"""

import random

def random_array(arr):
    """
    Fills the given array with random numbers between 1 and 20.

    Args:
        arr (list): A list to fill with random integers.

    Returns:
        list: The same list filled with random integers.
    """
    for i, _ in enumerate(arr):
        # Generate a random number between 1 and 20
        arr[i] = random.randint(1, 20)
    return arr

