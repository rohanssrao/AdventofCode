(ranges := sorted([[int(line.split('-')[0]), int(line.split('-')[1])+1] for line in open(0).read().split() if '-' in line ], key=lambda r: r[0]), [(b_prev := ranges[i-1][1], (ranges[i].__setitem__(0, b_prev), ranges[i].__setitem__(1, ranges[i][0]) if ranges[i][1] < ranges[i][0] else None) if a <= b_prev else None) for i, (a, b) in enumerate(ranges) if i != 0], print(sum(b-a for a,b in ranges)))


# (
#     ranges := sorted([
#         [int(line.split('-')[0]), int(line.split('-')[1])+1]
#         for line in open(0).read().split()
#         if '-' in line
#     ], key=lambda r: r[0]),
#     [
#         (
#             b_prev := ranges[i-1][1],
#             (
#                 ranges[i].__setitem__(0, b_prev),
#                 ranges[i].__setitem__(1, ranges[i][0]) if ranges[i][1] < ranges[i][0] else None
#             ) if a <= b_prev else None
#         )
#         for i, (a, b) in enumerate(ranges)
#         if i != 0
#     ],
#     print(sum(b-a for a,b in ranges))
# )

# ranges = []
#
# for line in open(0).read().split():
#     if '-' in line:
#         a, b = line.split('-')
#         ranges += [[int(a), int(b)+1]]
#
# ranges.sort(key=lambda r: r[0])
#
# for i, (a, b) in enumerate(ranges):
#     if i == 0: continue
#     b_prev = ranges[i-1][1]
#     if a <= b_prev:
#         ranges[i][0] = b_prev
#         if ranges[i][1] < ranges[i][0]:
#             ranges[i][1] = ranges[i][0]
#
# print(sum(b-a for a,b in ranges))
