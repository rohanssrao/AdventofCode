print((pos := 50, sum([(rotation := (1 if line[0] == 'R' else -1) * int(line[1:]), dest := pos+rotation, int(abs(dest / 100)) + (pos > 0 and dest <= 0), pos := dest % 100)[-2] for line in open(0).read().split()]))[-1])


# print(
#     (
#         pos := 50,
#         sum(
#             [
#                 (
#                     rotation := (1 if line[0] == 'R' else -1) * int(line[1:]),
#                     dest := pos+rotation,
#                     int(abs(dest / 100)) + (pos > 0 and dest <= 0),
#                     pos := dest % 100
#                 )[-2]
#                 for line in open(0).read().split()
#             ]
#         )
#     )[-1]
# )


# pos = 50
# count = 0
# for line in open(0).read().split():
#     rotation = (1 if line[0] == 'R' else -1) * int(line[1:])
#     dest = pos+rotation
#     count += int(abs(dest / 100)) + (pos > 0 and dest <= 0)
#     pos = dest % 100
# print(count)
