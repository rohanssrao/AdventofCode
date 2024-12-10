grid = [list(l) for l in open(0).readlines()]
y = [i for i, line in enumerate(grid) if '^' in line][0]
x = grid[y].index('^')
dir = (-1, 0)
visited = set((((y,x), dir),))

def traverse(grid, y, x, visited, dir):
    while True:
        y += dir[0]
        x += dir[1]
        if ((y,x), dir) in visited:
            return (True, visited)
        visited.add(((y,x), dir))
        if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0])):
            return (False, visited)
        if grid[y + dir[0]][x + dir[1]] == '#':
            dir = (dir[1], -dir[0]) 

visited = traverse(grid, y, x, visited, dir)[1]

count = 0
for pos in set(p[0] for p in visited):
    if pos != (y, x):
        grid[pos[0]][pos[1]] = '#'
        is_loop = traverse(grid, y, x, set((((y,x), dir),)), dir)[0]
        if is_loop:
            count += 1
            print(count)
        grid[pos[0]][pos[1]] = '.'

print(count)



# print((fn := lambda grid, y_orig, x_orig, y, x, visited, dir, loop, recurse: (
#
#     sum(int(fn(
#         [['#' if (y,x) == pos else grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))],
#         y_orig := y_orig,
#         x_orig := x_orig,
#         y := y_orig,
#         x := x_orig,
#         visited := [((y_orig,x_orig), (-1, 0))],
#         dir := (-1, 0),
#         loop := None,
#         recurse := False,
#     )) for pos in set(p[0] for p in visited) if (y_orig,x_orig) != pos) if recurse and loop is not None else loop if loop is not None else fn(
#         grid := grid,
#         y_orig := y_orig,
#         x_orig := x_orig,
#         y := y + dir[0],
#         x := x + dir[1],
#         visited := visited + [((y,x), dir)],
#         dir := None 
#             if not (0 <= y + dir[0] < len(grid) and 0 <= x + dir[1] < len(grid[0]))
#             else (dir[1], -dir[0]) if grid[y + dir[0]][x + dir[1]] == '#'
#             else dir,
#         loop := True if len(visited) != len(set(visited)) else False if dir is None else None,
#         recurse := recurse,
#     )
# ))(
#     grid := [list(l) for l in open(0).readlines()],
#     y_orig := [i for i, line in enumerate(grid) if '^' in line][0],
#     x_orig := grid[y_orig].index('^'),
#     y := y_orig,
#     x := x_orig,
#     visited := [((y,x), (-1, 0))],
#     dir := (-1, 0) if __import__('sys').setrecursionlimit(6000000) else (-1, 0),
#     loop := None,
#     recurse := True,
# ))
