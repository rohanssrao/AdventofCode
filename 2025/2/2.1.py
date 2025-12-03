print(sum([i for line in open(0).read().split(',') for a,b in (map(int, line.split('-')),) for i in range(a, b+1) if (s := str(i), length := len(s))[-1] % 2 == 0 and s[:length // 2] == s[length // 2:]]))


# print(
#     sum(
#         [
#             i
#             for line in open(0).read().split(',')
#             for a,b in (map(int, line.split('-')),)
#             for i in range(a, b+1)
#             if (s := str(i), length := len(s))[-1] % 2 == 0 and s[:length // 2] == s[length // 2:]
#         ]
#     )
# )


# total = 0
# for line in open(0).read().split(','):
#     a, b = map(int, line.split('-'))
#     for i in range(a, b+1):
#         s = str(i)
#         length = len(s)
#         if length % 2 != 0: continue
#         if s[:length // 2] == s[length // 2:]:
#             total += i
# print(total)
