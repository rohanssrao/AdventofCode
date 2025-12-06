(grid := [line.split() for line in open(0).read().splitlines()], print(sum(eval(grid[-1][x].join(grid[y][x] for y in range(len(grid[:-1])))) for x in range(len(grid[0])))))


# (
#     grid := [line.split() for line in open(0).read().splitlines()],
#     print(sum(eval(grid[-1][x].join(grid[y][x] for y in range(len(grid[:-1])))) for x in range(len(grid[0]))))
# )


# grid = [line.split() for line in open(0).read().splitlines()]
# print(sum(eval(grid[-1][x].join(grid[y][x] for y in range(len(grid[:-1])))) for x in range(len(grid[0]))))
