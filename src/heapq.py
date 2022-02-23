import heapq

my_heap = []
heapq.heappush(my_heap, 1)
heapq.heappush(my_heap, 5)
heapq.heappush(my_heap, 3)
print(f"heap: {my_heap}")
smallest = heapq.heappop(my_heap)
print(f"smallest: {smallest}")
print(f"heap: {my_heap}")

h_ii = [3, 4, 5]
s_ii = heapq.heappushpop(h_ii, 1)
print(f"{h_ii} {s_ii}")

h_ii = [3, 4, 5]
s_ii = heapq.heappushpop(h_ii, 4)
print(f"{h_ii} {s_ii}")

h_ii = [3, 4, 5]
s_ii = heapq.heappushpop(h_ii, 6)
print(f"{h_ii} {s_ii}")
print(f"{type(h_ii)}")

x = [1, 2]
heapq.heapify([1, 2])
print(type(x))

h = [1, 2, 3, 4, 5, 6]
n = heapq.nsmallest(3, h)
print(n)
