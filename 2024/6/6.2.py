print((fn := lambda dir, grid, y, x, start_pos, loop, visited, recurse: ( sum(int(fn( dir := (-1, 0), [['#' if (y,x) == pos else grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))], y := start_pos[0], x := start_pos[1], start_pos := start_pos, loop := None, visited := set(((start_pos, dir),)), recurse := False,)) for pos in set(p[0] for p in visited) if start_pos != pos) if recurse and loop is not None else loop if loop is not None else fn( dir := None if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])) else (dir[1], -dir[0]) if grid[y + dir[0]][x + dir[1]] == '#' else dir, grid := grid, y := y + dir[0] if dir and (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])) and grid[y + dir[0]][x + dir[1]] != '#' else y, x := x + dir[1] if dir and (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])) and grid[y + dir[0]][x + dir[1]] != '#' else x, start_pos := start_pos, loop := True if ((y,x), dir) in visited else False if dir is None else None, visited := visited | set((((y,x), dir),)), recurse := recurse,)))( dir := (-1, 0) if __import__('sys').setrecursionlimit(15000) else (-1, 0), grid := [list(l) for l in open(0).readlines()], y := [i for i, line in enumerate(grid) if '^' in line][0], x := grid[y].index('^'), start_pos := (y, x), loop := None, visited := set((((y,x), dir),)), recurse := True,))

# print((fn := lambda dir, grid, y, x, start_pos, loop, visited, recurse: (
#     sum(int(fn(
#         dir := (-1, 0),
#         [['#' if (y,x) == pos else grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))],
#         y := start_pos[0],
#         x := start_pos[1],
#         start_pos := start_pos,
#         loop := None,
#         visited := set(((start_pos, dir),)),
#         recurse := False,
#     )) for pos in set(p[0] for p in visited) if start_pos != pos) if recurse and loop is not None else loop if loop is not None else fn(
#         dir := None
#             if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0]))
#             else (dir[1], -dir[0]) if grid[y + dir[0]][x + dir[1]] == '#'
#             else dir,
#         grid := grid,
#         y := y + dir[0] if dir and (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])) and grid[y + dir[0]][x + dir[1]] != '#' else y,
#         x := x + dir[1] if dir and (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])) and grid[y + dir[0]][x + dir[1]] != '#' else x,
#         start_pos := start_pos,
#         loop := True if ((y,x), dir) in visited else False if dir is None else None,
#         visited := visited | set((((y,x), dir),)),
#         recurse := recurse,
#     )
# ))(
#     dir := (-1, 0) if __import__('sys').setrecursionlimit(15000) else (-1, 0),
#     grid := [list(l) for l in open(0).readlines()],
#     y := [i for i, line in enumerate(grid) if '^' in line][0],
#     x := grid[y].index('^'),
#     start_pos := (y, x),
#     loop := None,
#     visited := set((((y,x), dir),)),
#     recurse := True,
# ))


# # normal solution
# 
# grid = [list(l) for l in open(0).readlines()]
# y = [i for i, line in enumerate(grid) if '^' in line][0]
# x = grid[y].index('^')
# dir = (-1, 0)
# visited = set((((y,x), dir),))
#
# def traverse(grid, y, x, visited, dir):
#     while True:
#         if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])):
#             return (False, visited)
#         if grid[y + dir[0]][x + dir[1]] == '#':
#             dir = (dir[1], -dir[0]) 
#         else:
#             y += dir[0]
#             x += dir[1]
#             if ((y,x), dir) in visited:
#                 return (True, visited)
#             visited.add(((y,x), dir))
#
# visited = traverse(grid, y, x, visited, dir)[1]
#
# count = 0
# for pos in set(p[0] for p in visited):
#     if pos != (y, x):
#         grid[pos[0]][pos[1]] = '#'
#         is_loop = traverse(grid, y, x, set((((y,x), dir),)), dir)[0]
#         if is_loop:
#             count += 1
#         grid[pos[0]][pos[1]] = '.'
#
# print(count)
#
