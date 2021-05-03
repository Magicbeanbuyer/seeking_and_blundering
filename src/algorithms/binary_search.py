"""implement binary search."""
from typing import Optional


def binary_search(pool: list, target) -> Optional[int]:
    """Search for a target in a list, using binary search.

    Args:
        pool (list): a pool of all elements being searched.
        target: the target being searched.

    Returns:
    int: the index of the target.
    """
    sorted_pool = sorted(pool)
    low = 0
    high = len(sorted_pool) - 1
    while low + 1 != high:
        mid = (low + high) // 2
        if sorted_pool[mid] == target:
            return mid
        if sorted_pool[mid] < target:
            low = mid
        else:
            high = mid
    return None


my_target = binary_search([1, 2, 3], 3)
print(my_target)
