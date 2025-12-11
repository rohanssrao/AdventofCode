# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "numpy",
#     "pulp",
# ]
# ///

print(sum((split_line := line.split(" "), buttons := split_line[1:-1], joltages := split_line[-1], joltages := list(map(int, joltages[1:-1].split(","))), buttons := [ [1 if i in map(int, b[1:-1].split(",")) else 0 for i in range(len(joltages)) ] for b in buttons ], A := __import__("numpy").column_stack(buttons), x := [ __import__("pulp").LpVariable(str(i), 0, None, "Integer") for i in range(len(buttons)) ], prob := __import__("pulp").LpProblem(), [ prob.__iadd__(__import__("pulp").lpDot(A[i], x) == bi) for i, bi in enumerate(joltages) ], prob.__iadd__(__import__("pulp").lpSum(x)), prob.solve(__import__("pulp").PULP_CBC_CMD(msg=0)), sum([int(v.value()) for v in x]))[-1] for line in open(0).read().splitlines()))


# print(sum(
#     (
#         split_line := line.split(" "),
#         buttons := split_line[1:-1],
#         joltages := split_line[-1],
#         joltages := list(map(int, joltages[1:-1].split(","))),
#         buttons := [ [1 if i in map(int, b[1:-1].split(",")) else 0 for i in range(len(joltages)) ] for b in buttons ],
#         A := __import__("numpy").column_stack(buttons),
#         x := [ __import__("pulp").LpVariable(str(i), 0, None, "Integer") for i in range(len(buttons)) ],
#         prob := __import__("pulp").LpProblem(),
#         [
#             prob.__iadd__(__import__("pulp").lpDot(A[i], x) == bi)
#             for i, bi in enumerate(joltages)
#         ],
#         prob.__iadd__(__import__("pulp").lpSum(x)),
#         prob.solve(__import__("pulp").PULP_CBC_CMD(msg=0)),
#         sum([int(v.value()) for v in x])
#     )[-1]
#     for line in open(0).read().splitlines()
# ))


# from pulp import *
# import numpy as np
#
# total = 0
#
# for line in open(0).read().splitlines():
#     _, *buttons, joltages = line.split(" ")
#     joltages = list(map(int, joltages[1:-1].split(",")))
#     buttons = [ [1 if i in map(int, b[1:-1].split(",")) else 0 for i in range(len(joltages)) ] for b in buttons ]
#
#     A = np.column_stack(buttons)
#     x = [ LpVariable(str(i), 0, None, "Integer") for i in range(len(buttons)) ]
#     prob = LpProblem()
#     for i, bi in enumerate(joltages):
#         prob += lpDot(A[i], x) == bi
#     prob += lpSum(x)
#     prob.solve(PULP_CBC_CMD(msg=0))
#     total += sum([int(v.value()) for v in x])
#
# print(total)
