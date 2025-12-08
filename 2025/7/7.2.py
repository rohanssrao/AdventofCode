(grid := open(0).read().split(), tachyons := {grid[0].index('S'): 1}, [([tachyons.__setitem__(n, tachyons.get(n, 0) + tachyons[t]) for n in (t-1, t+1)], tachyons.__setitem__(t, 0)) for row in grid[1:] for t in list(tachyons) if row[t] == '^'], print(sum(tachyons.values())))


# (
#     grid := open(0).read().split(),
#     tachyons := {grid[0].index('S'): 1},
#     [
#         (
#             [tachyons.__setitem__(n, tachyons.get(n, 0) + tachyons[t]) for n in (t-1, t+1)],
#             tachyons.__setitem__(t, 0)
#         )
#         for row in grid[1:]
#         for t in list(tachyons)
#         if row[t] == '^'
#     ],
#     print(sum(tachyons.values()))
# )


# grid = open(0).read().split()
# tachyons = {grid[0].index('S'): 1}
#
# for row in grid[1:]:
#     for t in list(tachyons):
#         if row[t] == '^':
#             for n in (t-1, t+1):
#                 tachyons[n] = tachyons.get(n, 0) + tachyons[t]
#             tachyons[t] = 0
#
# print(sum(tachyons.values()))
