(inputs := open(0).read().split('\n\n'), grid := inputs[0], movements := inputs[1], grid := [[c for c in l] for l in str(grid).splitlines()], movements := [m for m in movements if m != '\n'], y := [i for i, line in enumerate(grid) if '@' in line][0], x := grid[y].index('@'), [(dir := (-1,0) if m == '^' else (0,1) if m == '>' else (1,0) if m == 'v' else (0,-1), dy := dir[0], dx := dir[1], d := 0, list(iter(lambda: (globals().__setitem__("d", d+1), c := grid[y+d*dy][x+d*dx], globals().__setitem__("d", 0) if c == '#' else None if c == '.' else True)[-1], None)), [[[old_y := y+i*dy, old_x := x+i*dx, new_y := old_y-dy, new_x := old_x-dx, grid[old_y].__setitem__(old_x, grid[new_y][new_x])] for i in reversed(range(d+1))], grid[y].__setitem__(x, '.'), y := y+dy, x := x+dx] if d else None) for m in movements], print(sum(100*i + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'O')))

# grid, movements = open(0).read().split('\n\n')
#
# grid = [[c for c in l] for l in str(grid).splitlines()]
# movements = [m for m in movements if m != '\n']
#
# y = [i for i, line in enumerate(grid) if '@' in line][0]
# x = grid[y].index('@')
#
# for m in movements:
#
#     dy, dx = (-1,0) if m == '^' else (0,1) if m == '>' else (1,0) if m == 'v' else (0,-1)
#
#     d = 0
#
#     list(iter(
#         lambda: (
#             globals().__setitem__("d", d+1),
#             c := grid[y+d*dy][x+d*dx],
#             globals().__setitem__("d", 0) if c == '#' else None if c == '.' else True
#         )[-1], None
#     ))
#
#     if d:
#         for i in reversed(range(d+1)):
#             old_y, old_x = y+i*dy, x+i*dx
#             new_y, new_x = old_y-dy, old_x-dx
#             grid[old_y][old_x] = grid[new_y][new_x]
#         grid[y][x] = '.'
#         y, x = y+dy, x+dx
#
# print(sum(100*i + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'O'))
