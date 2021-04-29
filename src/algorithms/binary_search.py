def binary_search(pool: list, target):
    """write a very loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooog description"""
    sorted_pool = sorted(pool)
    low = 0
    high = len(sorted_pool) - 1
    while low + 1 != high:
        mid = (low + high) // 2
        if sorted_pool[mid] == target:
            return mid
        elif sorted_pool[mid] < target:
            low = mid
        else:
            high = mid
    print(
        f"loooooooooooooooooooooooooooooooooooooooooooooooooo oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooog"
    )
    return None


# TODO: test before commit
binary_search([1, 2, 3], 3)
