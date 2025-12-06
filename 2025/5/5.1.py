(ranges := set(), print(sum((r := line.split('-'), a := int(r[0]), b := int(r[1])+1, ranges.add(range(a, b)), False)[-1] if '-' in line else (id := int(line), any(id in r for r in ranges))[-1] for line in open(0).read().split())))


# (
#     ranges := set(),
#     print(sum(
#         (
#             r := line.split('-'),
#             a := int(r[0]),
#             b := int(r[1])+1,
#             ranges.add(range(a, b)),
#             False
#         )[-1] if '-' in line else (
#             id := int(line),
#             any(id in r for r in ranges)
#         )[-1]
#         for line in open(0).read().split()
#     ))
# )

# ranges = set()
# count = 0
#
# for line in open(0).read().split():
#     if '-' in line:
#         a, b = line.split('-')
#         ranges.add(range(int(a), int(b)+1))
#     else:
#         id = int(line)
#         if any(id in r for r in ranges):
#             count += 1
#
# print(count)
