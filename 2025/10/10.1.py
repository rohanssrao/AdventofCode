(powerset := lambda iterable: __import__("itertools").chain.from_iterable(__import__("itertools").combinations(list(iterable), r) for r in range(1, len(list(iterable))+1)), print(sum((split_line := line.split(" "), diagram := [ False if l == '.' else True for l in split_line[0][1:-1] ], buttons := [ list(map(int, b[1:-1].split(","))) for b in split_line[1:-1] ], min((lights := [ False ] * len(diagram), [ lights.__setitem__(idx, not lights[idx]) for press in combo for idx in press ], len(combo) if lights == diagram else 1000)[-1] for combo in powerset(buttons)))[-1] for line in open(0).read().splitlines())))


# (
#     powerset := lambda iterable:
#         __import__("itertools").chain.from_iterable(__import__("itertools").combinations(list(iterable), r) for r in range(1, len(list(iterable))+1)),
#     print(sum(
#         (
#             split_line := line.split(" "),
#             diagram := [ False if l == '.' else True for l in split_line[0][1:-1] ],
#             buttons := [ list(map(int, b[1:-1].split(","))) for b in split_line[1:-1] ],
#             min(
#                 (
#                     lights := [ False ] * len(diagram),
#                     [
#                         lights.__setitem__(idx, not lights[idx])
#                         for press in combo
#                         for idx in press
#                     ],
#                     len(combo) if lights == diagram else 1000
#                 )[-1]
#                 for combo in powerset(buttons)
#             )
#         )[-1]
#         for line in open(0).read().splitlines()
#     ))
# )


# from itertools import chain, combinations
#
# def powerset(iterable):
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))
#
# total = 0
#
# for line in open(0).read().splitlines():
#     diagram, *buttons, _ = line.split(" ")
#     diagram = [ False if l == '.' else True for l in diagram[1:-1] ]
#     buttons = [ list(map(int, b[1:-1].split(","))) for b in buttons ]
#     min_presses = 1000
#     for combo in powerset(buttons):
#         lights = [ False ] * len(diagram)
#         for press in combo:
#             for idx in press:
#                 lights[idx] = not lights[idx]
#         if lights == diagram:
#             min_presses = min(min_presses, len(combo))
#     total += min_presses
#
# print(total)
