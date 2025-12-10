(tiles := [tuple(map(int, line.split(","))) for line in open(0).read().split()], print(max((abs(x2-x1)+1)*(abs(y2-y1)+1) for x1, y1 in tiles for x2, y2 in tiles)))


# (
#     tiles := [tuple(map(int, line.split(","))) for line in open(0).read().split()],
#     print(max(
#         (abs(x2-x1)+1)*(abs(y2-y1)+1)
#         for x1, y1 in tiles
#         for x2, y2 in tiles
#     ))
# )


# tiles = [tuple(map(int, line.split(","))) for line in open(0).read().split()]
#
# print(max(
#     (abs(x2-x1)+1)*(abs(y2-y1)+1)
#     for x1, y1 in tiles
#     for x2, y2 in tiles
# ))
