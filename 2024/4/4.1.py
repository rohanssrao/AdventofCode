print(sum([0 <= y+3*y_d < len(grid) and 0 <= x+3*x_d < len(grid[0]) and "".join(grid[y+i*y_d][x+i*x_d] for i in range(4)) == "XMAS" for grid in ([l.strip() for l in open(0).readlines()],) for y in range(len(grid)) for x in range(len(grid[0])) for y_d in (-1,0,1) for x_d in (-1,0,1)]))