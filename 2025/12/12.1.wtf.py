print(sum(board_size >= 9*num_shapes for board_size, num_shapes in [(__import__("math").prod((map(int, line.split(":")[0].split("x")))), sum(map(int, line.split(" ")[1:]))) for line in open(0).read().splitlines() if "x" in line]))


# print(
#     sum(
#         board_size >= 9*num_shapes
#         for board_size, num_shapes in [
#             (
#                 __import__("math").prod((map(int, line.split(":")[0].split("x")))),
#                 sum(map(int, line.split(" ")[1:]))
#             )
#             for line in open(0).read().splitlines()
#             if "x" in line
#         ]
#     )
# )


# boards = []
# num_shapes = []
#
# for line in open(0).read().splitlines():
#     if "x" in line:
#         boards.append(tuple(map(int, line.split(":")[0].split("x"))))
#         num_shapes.append(sum(map(int, line.split(" ")[1:])))
#
# total = 0
# for board, n in zip(boards, num_shapes):
#     if board[0] * board[1] >= 9*n:
#         total += 1
#
# print(total)
