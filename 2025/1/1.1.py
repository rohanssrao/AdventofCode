print((pos := 50, sum([(pos := (pos + (1 if line[0] == 'R' else -1) * int(line[1:])) % 100) == 0 for line in open(0).read().split()]))[-1])


# print(
#     (
#         pos := 50,
#         sum(
#             [
#                 (pos := (pos + (1 if line[0] == 'R' else -1) * int(line[1:])) % 100) == 0
#                 for line in open(0).read().split()
#             ]
#         )
#     )[-1]
# )


# pos = 50
# count = 0
# for line in open(0).read().split():
#     pos = (pos + (1 if line[0] == 'R' else -1) * int(line[1:])) % 100
#     if pos == 0:
#         count += 1
# print(count)
