(junctions := [tuple(map(int, line.split(','))) for line in open(0).read().split()], circuits := {(j,) for j in junctions}, x_product := 0, pairs := sorted([((x1, y1, z1), (x2, y2, z2)) for i1, (x1,y1,z1) in enumerate(junctions) for i2, (x2,y2,z2) in enumerate(junctions[i1+1:])], key=lambda pair: __import__("math").sqrt(pow(pair[1][0]-pair[0][0], 2) + pow(pair[1][1]-pair[0][1], 2) + pow(pair[1][2]-pair[0][2], 2))), [(j1_circuit := next(filter(lambda c: pair[0] in c, circuits)), j2_circuit := next(filter(lambda c: pair[1] in c, circuits)), (circuits.remove(j1_circuit), circuits.remove(j2_circuit), circuits.add(j1_circuit + j2_circuit), x_product := pair[0][0] * pair[1][0]) if j1_circuit != j2_circuit else None) for pair in pairs], print(x_product))


# (
#     junctions := [
#         tuple(map(int, line.split(',')))
#         for line in open(0).read().split()
#     ],
#     circuits := { (j,) for j in junctions },
#     x_product := 0,
#     pairs := sorted([
#         ((x1, y1, z1), (x2, y2, z2))
#         for i1, (x1,y1,z1) in enumerate(junctions)
#         for i2, (x2,y2,z2) in enumerate(junctions[i1+1:])
#     ], key=lambda pair: __import__("math").sqrt(pow(pair[1][0]-pair[0][0], 2) + pow(pair[1][1]-pair[0][1], 2) + pow(pair[1][2]-pair[0][2], 2))),
#     [
#         (
#             j1_circuit := next(filter(lambda c: pair[0] in c, circuits)),
#             j2_circuit := next(filter(lambda c: pair[1] in c, circuits)),
#             (
#                 circuits.remove(j1_circuit),
#                 circuits.remove(j2_circuit),
#                 circuits.add(j1_circuit + j2_circuit),
#                 x_product := pair[0][0] * pair[1][0]
#             )
#             if j1_circuit != j2_circuit else None
#         )
#         for pair in pairs
#     ],
#     print(x_product)
# )


# import math
#
# junctions = [
#     tuple(map(int, line.split(',')))
#     for line in open(0).read().split()
# ]
#
# circuits = { (j,) for j in junctions }
#
# pairs = sorted([
#     ((x1, y1, z1), (x2, y2, z2))
#     for i1, (x1,y1,z1) in enumerate(junctions)
#     for i2, (x2,y2,z2) in enumerate(junctions[i1+1:])
# ], key=lambda pair: math.sqrt(pow(pair[1][0]-pair[0][0], 2) + pow(pair[1][1]-pair[0][1], 2) + pow(pair[1][2]-pair[0][2], 2)))
#
# x_product = None
#
# for pair in pairs:
#     j1_circuit = next(filter(lambda c: pair[0] in c, circuits))
#     j2_circuit = next(filter(lambda c: pair[1] in c, circuits))
#     if j1_circuit != j2_circuit:
#         circuits.remove(j1_circuit)
#         circuits.remove(j2_circuit)
#         circuits.add(j1_circuit + j2_circuit)
#         x_product = pair[0][0] * pair[1][0]
#
# print(x_product)
