from typing import List

#
# def depth_first_search(grid: List[str], x, y):
#     print(x, y ,"\n")
#     length = len(grid)
#     width = len(grid[0])
#
#
#     if grid[x][y] != "1":  # water or visited
#         return
#     if y < 0:  # reached bottom
#         return
#     if y >= length:  # reached top
#         return
#     if x < 0:  # reached left
#         return
#     if x >= width:  # reached right
#         return
#
#     grid[x][y] = "2"  # mark visited
#     print(x, y, "===")
#     print("right")
#     depth_first_search(grid, x, y + 1)  # move right
#     print(x, y, "===")
#     print("down")
#     depth_first_search(grid, x + 1, y)  # move down
#     print(x, y, "===")
#     print("up")
#     depth_first_search(grid, x - 1, y)  # move up
#     print(x, y, "===")
#     print("left")
#     depth_first_search(grid, x, y - 1)  # move left
#
#
# def count_islands(grid: List[str]) -> int:
#     length = len(grid)
#     width = len(grid[0])
#     cnt = 0
#
#     for y in range(length):
#         for x in range(width):
#             if grid[y][x] == "1":
#                 depth_first_search(grid, x, y)
#                 cnt += 1
#     return cnt


def numIslands(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    print(i, j, "\n")
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        return
    grid[i][j] = "#"
    print("===", i, j)
    print("down")
    dfs(grid, i + 1, j)
    print("up")
    dfs(grid, i - 1, j)
    print("right")
    dfs(grid, i, j + 1)
    print("left")
    dfs(grid, i, j - 1)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

a = numIslands(grid)
print(a)
