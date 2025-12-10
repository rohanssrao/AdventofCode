# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "shapely",
# ]
# ///

(red_tiles := [tuple(map(int, line.split(","))) for line in open(0).read().split()], polygon := __import__("shapely.geometry.polygon").Polygon(red_tiles), print(max((abs(x2-x1)+1)*(abs(y2-y1)+1) for i, (x1, y1) in enumerate(red_tiles) for x2, y2 in red_tiles[i+1:] if polygon.contains(__import__("shapely.geometry.polygon").Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])))))


# (
#     red_tiles := [tuple(map(int, line.split(","))) for line in open(0).read().split()],
#     polygon := __import__("shapely.geometry.polygon").Polygon(red_tiles),
#     print(max(
#         (abs(x2-x1)+1)*(abs(y2-y1)+1)
#         for i, (x1, y1) in enumerate(red_tiles)
#         for x2, y2 in red_tiles[i+1:]
#         if polygon.contains(__import__("shapely.geometry.polygon").Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)]))
#     ))
# )


# from shapely.geometry.polygon import Polygon
#
# red_tiles = [tuple(map(int, line.split(","))) for line in open(0).read().split()]
#
# polygon = Polygon(red_tiles)
#
# max_area = 0
#
# for i, (x1, y1) in enumerate(red_tiles):
#     for x2, y2 in red_tiles[i+1:]:
#         polygon2 = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
#         if polygon.contains(polygon2):
#             max_area = max(max_area, (abs(x2-x1)+1)*(abs(y2-y1)+1))
#
# print(max_area)
