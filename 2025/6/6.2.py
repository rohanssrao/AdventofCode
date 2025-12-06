(grid := [list(line) for line in open(0).read().splitlines()], nums := [], print(sum([(num := ''.join([grid[y][x] for y in range(len(grid))]), nums.append(num[:-1]) if num.strip() else None, (eval(num[-1].join(nums)), nums := [])[0] if num[-1] != " " else 0)[-1] for x in reversed(range(len(grid[0])))])))


# (
#     grid := [list(line) for line in open(0).read().splitlines()],
#     nums := [],
#     print(sum([
#         (
#             num := ''.join([grid[y][x] for y in range(len(grid))]),
#             nums.append(num[:-1]) if num.strip() else None,
#             (
#                 eval(num[-1].join(nums)),
#                 nums := []
#             )[0] if num[-1] != " " else 0
#         )[-1]
#         for x in reversed(range(len(grid[0])))
#     ]))
# )


# grid = [list(line) for line in open(0).read().splitlines()]
#
# total = 0
# nums = []
#
# for x in reversed(range(len(grid[0]))):
#     num = ''.join([grid[y][x] for y in range(len(grid))])
#     if not num.strip():
#         continue
#     nums.append(num[:-1])
#     if num[-1] != " ":
#         total += eval(num[-1].join(nums))
#         nums = []
#
# print(total)
