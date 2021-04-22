
def binary_search(pool: list, target):
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
    return None
