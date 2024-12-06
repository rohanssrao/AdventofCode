print((fn := lambda grid, y, x, visited, dir: ( len(visited) if not dir else fn( grid := grid, y := y + dir[0], x := x + dir[1], visited := visited | set([(y,x)]), dir := None if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])) else (dir[1], -dir[0]) if grid[y + dir[0]][x + dir[1]] == '#' else dir,)))( grid := [list(l) for l in open(0).readlines()], y := [i for i, line in enumerate(grid) if '^' in line][0], x := grid[y].index('^'), visited := set([(y,x)]), dir := (-1, 0) if __import__('sys').setrecursionlimit(6000) else (-1, 0),))

# print((fn := lambda grid, y, x, visited, dir: (
#     len(visited) if not dir else fn(
#         grid := grid,
#         y := y + dir[0],
#         x := x + dir[1],
#         visited := visited | set([(y,x)]),
#         dir := None 
#             if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0]))
#             else (dir[1], -dir[0]) if grid[y + dir[0]][x + dir[1]] == '#'
#             else dir,
#     )
# ))(
#     grid := [list(l) for l in open(0).readlines()],
#     y := [i for i, line in enumerate(grid) if '^' in line][0],
#     x := grid[y].index('^'),
#     visited := set([(y,x)]),
#     dir := (-1, 0) if __import__('sys').setrecursionlimit(6000) else (-1, 0),
# ))
