(grid := [list(map(int, list(l))) for l in open(0).read().splitlines()], zeros := [(i, j) for i,_ in enumerate(grid) for j,_ in enumerate(grid[0]) if grid[i][j] == 0], rec := lambda grid, visited, y, x: 1 if grid[y][x] == 9 else sum([rec(grid, visited.union({(y2,x2)}), y2, x2) for y2,x2 in [(y-1,x), (y, x+1), (y+1, x), (y, x-1)] if 0 <= y2 < len(grid) and 0 <= x2 < len(grid[0]) and (y2,x2) not in visited and grid[y2][x2] == grid[y][x] + 1]), print(sum(rec(grid, {z}, z[0], z[1]) for z in zeros)))
