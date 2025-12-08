(grid := open(0).read().split(), tachyons := {grid[0].index('S')}, print(len([(tachyons.remove(t), tachyons.update({t-1, t+1})) for row in grid[1:] for t in list(tachyons) if row[t] == '^'])))


# (
#     grid := open(0).read().split(),
#     tachyons := {grid[0].index('S')},
#     print(len([
#         (
#             tachyons.remove(t),
#             tachyons.update({t-1, t+1})
#         )
#         for row in grid[1:]
#         for t in list(tachyons)
#         if row[t] == '^'
#     ]))
# )


# grid = open(0).read().split()
# tachyons = {grid[0].index('S')}
# splits = 0
#
# for row in grid[1:]:
#     for t in list(tachyons):
#         if row[t] == '^':
#             tachyons.remove(t)
#             tachyons |= {t-1, t+1}
#             splits += 1
#
# print(splits)
