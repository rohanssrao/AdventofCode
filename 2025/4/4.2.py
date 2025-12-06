(grid := [list(row) for row in open(0).read().split()], get_adjacents := lambda grid, y, x: [(y+y_dir, x+x_dir) for y_dir in [-1, 0, 1] for x_dir in [-1, 0, 1] if (y_dir, x_dir) != (0, 0) and 0 <= y+y_dir < len(grid) and 0 <= x+x_dir < len(grid[0]) and grid[y+y_dir][x+x_dir] not in (None, '.')], grid := [[len(get_adjacents(grid, y, x)) if chr == '@' else None for x, chr in enumerate(row) ] for y, row in enumerate(grid)], total_removed := 0, removed_this_turn := None, list(iter(lambda: (removed_this_turn := 0, new_grid := [row[:] for row in globals().__getitem__("grid")], removed_this_turn := removed_this_turn + sum((new_grid[y].__setitem__(x, None), [new_grid[adj_y].__setitem__(adj_x, new_grid[adj_y][adj_x] - 1) for adj_y, adj_x in get_adjacents(grid, y, x) if new_grid[adj_y][adj_x] is not None], 1)[-1] for y, row in enumerate(grid) for x, chr in enumerate(row) if chr is not None and chr < 4), globals().__setitem__("total_removed", globals().__getitem__("total_removed") + removed_this_turn), globals().__setitem__("grid", new_grid), removed_this_turn)[-1], 0)), print(total_removed))


# (
#     grid := [list(row) for row in open(0).read().split()],
#     get_adjacents := lambda grid, y, x:
#         [
#             (y+y_dir, x+x_dir)
#             for y_dir in [-1, 0, 1]
#             for x_dir in [-1, 0, 1]
#             if (y_dir, x_dir) != (0, 0)
#                 and 0 <= y+y_dir < len(grid)
#                 and 0 <= x+x_dir < len(grid[0])
#                 and grid[y+y_dir][x+x_dir] not in (None, '.')
#         ],
#     grid := [
#         [len(get_adjacents(grid, y, x)) if chr == '@' else None for x, chr in enumerate(row)]
#         for y, row in enumerate(grid)
#     ],
#     total_removed := 0,
#     removed_this_turn := None,
#     list(iter(
#         lambda:
#         (
#             removed_this_turn := 0,
#             new_grid := [row[:] for row in globals().__getitem__("grid")],
#             removed_this_turn := removed_this_turn + sum(
#                 (
#                     new_grid[y].__setitem__(x, None),
#                     [
#                         new_grid[adj_y].__setitem__(adj_x, new_grid[adj_y][adj_x] - 1)
#                         for adj_y, adj_x in get_adjacents(grid, y, x)
#                         if new_grid[adj_y][adj_x] is not None
#                     ],
#                     1
#                 )[-1]
#                 for y, row in enumerate(grid)
#                 for x, chr in enumerate(row)
#                 if chr is not None and chr < 4
#             ),
#             globals().__setitem__("total_removed", globals().__getitem__("total_removed") + removed_this_turn),
#             globals().__setitem__("grid", new_grid),
#             removed_this_turn
#         )[-1], 0
#     )),
#     print(total_removed)
# )


# grid = [list(row) for row in open(0).read().split()]
#
# def get_adjacents(grid, y, x):
#     adjacents = set()
#     for y_dir in [-1, 0, 1]:
#         for x_dir in [-1, 0, 1]:
#             if (y_dir, x_dir) == (0, 0): continue
#             if 0 <= y+y_dir < len(grid) and 0 <= x+x_dir < len(grid[0]) and grid[y+y_dir][x+x_dir] not in (None, '.'):
#                 adjacents.add((y+y_dir, x+x_dir))
#     return adjacents
#
# grid = [
#     [ len(get_adjacents(grid, y, x)) if chr == '@' else None for x, chr in enumerate(row) ]
#     for y, row in enumerate(grid)
# ]
#
# total_removed = 0
# removed_this_turn = None
#
#
# while removed_this_turn != 0:
#     removed_this_turn = 0
#     new_grid = [row[:] for row in grid]
#     for y, row in enumerate(grid):
#         for x, chr in enumerate(row):
#             if chr is None: continue
#             if chr < 4:
#                 new_grid[y][x] = None
#                 for adj_y, adj_x in get_adjacents(grid, y, x):
#                     if new_grid[adj_y][adj_x] is not None:
#                         new_grid[adj_y][adj_x] -= 1
#                 removed_this_turn += 1
#     total_removed += removed_this_turn
#     grid = new_grid
#
# print(total_removed)
