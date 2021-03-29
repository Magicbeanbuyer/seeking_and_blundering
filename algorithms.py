def binary_search(pool: list, target):
	sorted_pool = sorted(pool)
	low = 0
	high = len(sorted_pool) - 1
	mid = (low + high) // 2
	while low + 1 != high:
		if sorted_pool[mid] == target:
			return mid
		elif sorted_pool[mid] < target:
			low = mid
			mid = (low + high) // 2
		else:
			high = mid
			mid = (low + high) // 2
	return None
