(grid := [list(row) for row in open(0).read().split()], print(sum(chr == '@' and len([grid[y+y_dir][x+x_dir] for y_dir in [-1, 0, 1] for x_dir in [-1, 0, 1] if (y_dir, x_dir) != (0, 0) and 0 <= y+y_dir < len(grid) and 0 <= x+x_dir < len(grid[0]) and grid[y+y_dir][x+x_dir] == '@']) < 4 for y, row in enumerate(grid) for x, chr in enumerate(row))))


# (
#     grid := [list(row) for row in open(0).read().split()],
#     print(sum(
#         chr == '@' and len([
#             grid[y+y_dir][x+x_dir]
#             for y_dir in [-1, 0, 1]
#             for x_dir in [-1, 0, 1]
#             if (y_dir, x_dir) != (0, 0)
#                 and 0 <= y+y_dir < len(grid)
#                 and 0 <= x+x_dir < len(grid[0])
#                 and grid[y+y_dir][x+x_dir] == '@'
#         ]) < 4
#         for y, row in enumerate(grid)
#         for x, chr in enumerate(row)
#     ))
# )


# grid = [list(row) for row in open(0).read().split()]
# total = 0
#
# def get_adjacents(grid, y, x):
#     adjacents = []
#     for y_dir in [-1, 0, 1]:
#         for x_dir in [-1, 0, 1]:
#             if (y_dir, x_dir) == (0, 0): continue
#             if 0 <= y+y_dir < len(grid) and 0 <= x+x_dir < len(grid[0]):
#                 adjacents += grid[y+y_dir][x+x_dir]
#     return adjacents
#
# for y, row in enumerate(grid):
#     for x, chr in enumerate(row):
#         if chr == '@' and get_adjacents(grid, y, x).count('@') < 4:
#             total += 1
#
# print(total)
