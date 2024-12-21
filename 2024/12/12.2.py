(grid := [list(l) for l in open(0).read().splitlines()], grid_get := lambda p: grid[p[0]][p[1]] if 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]) else None, visited := set(), region := lambda y, x: (visited.add((y,x)), cells := [c for c in [(y-1,x), (y, x+1), (y+1, x), (y, x-1)] if grid_get(c) == grid_get((y,x)) and c not in visited], set([(y,x)]).union(*[region(*c) for c in cells]) if cells else set([(y,x)]))[-1], regions := set(), [regions.add(frozenset(region(y, x))) for y in range(len(grid)) for x in range(len(grid[0])) if not any((y,x) in r for r in regions)], print(sum(sum((neighbors := [(y-1,x), (y, x+1), (y+1, x), (y, x-1)], consecutive_neighbors := [(neighbors[i], neighbors[(i + 1) % len(neighbors)]) for i in range(len(neighbors))], corners := [(y-1,x+1), (y+1, x+1), (y+1, x-1), (y-1, x-1)], sum((grid_get(n1) != grid_get((y,x)) and grid_get(n2) != grid_get((y,x))) or (grid_get(n1) == grid_get((y,x)) and grid_get(n2) == grid_get((y,x)) and grid_get(corner) != grid_get((y,x))) for (n1, n2), corner in zip(consecutive_neighbors, corners)))[-1] for y,x in r) * len(r) for r in regions)))

# grid = [list(l) for l in open(0).read().splitlines()]
#
# grid_get = lambda p: grid[p[0]][p[1]] if 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]) else None
#
# visited = set()
#
# region = lambda y, x: (visited.add((y,x)), cells := [c for c in [(y-1,x), (y, x+1), (y+1, x), (y, x-1)] if grid_get(c) == grid_get((y,x)) and c not in visited], set([(y,x)]).union(*[region(*c) for c in cells]) if cells else set([(y,x)]))[-1]
#
# regions = set()
#
# [regions.add(frozenset(region(y, x))) for y in range(len(grid)) for x in range(len(grid[0])) if not any((y,x) in r for r in regions)]
#
# print(sum(
#     sum(
#         (
#             neighbors := [(y-1,x), (y, x+1), (y+1, x), (y, x-1)],
#             consecutive_neighbors := [(neighbors[i], neighbors[(i + 1) % len(neighbors)]) for i in range(len(neighbors))],
#             corners := [(y-1,x+1), (y+1, x+1), (y+1, x-1), (y-1, x-1)],
#             sum(
#                 ( grid_get(n1) != grid_get((y,x)) and grid_get(n2) != grid_get((y,x)))
#                 or
#                 ( grid_get(n1) == grid_get((y,x)) and grid_get(n2) == grid_get((y,x)) and grid_get(corner) != grid_get((y,x)) )
#                 for (n1, n2), corner in zip(consecutive_neighbors, corners)
#             )
#         )[-1]
#         for y,x in r
#     ) * len(r)
#     for r in regions
# ))
