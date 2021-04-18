from src.algorithms.binary_search import binary_search


def test_binary_search():
	pool_i = [1, 2, 2, 3]
	pool_ii = [1, 2, 2, 2, 3]
	assert binary_search(pool_i, 2) == 1
	assert binary_search(pool_i, 0) is None
	assert binary_search(pool_i, 4) is None
	assert binary_search(pool_ii, 2) == 2
