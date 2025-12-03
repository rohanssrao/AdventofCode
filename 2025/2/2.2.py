print((invalids := set(), total := 0, sum([(invalids.add(i), i)[-1] for line in open(0).read().split(',') for a,b in (map(int, line.split('-')),) for i in range(a, b+1) for s in (str(i),) for length in (len(s),) for seq_len in range(1, length // 2 + 1) if i not in invalids and length % seq_len == 0 and len(set([s[seq_len*n:seq_len*(n+1)] for n in range(0, length // seq_len)])) == 1]))[-1])

# print(
#     (
#         invalids := set(),
#         total := 0,
#         sum(
#             [
#                 (invalids.add(i), i)[-1]
#                 for line in open(0).read().split(',')
#                 for a,b in (map(int, line.split('-')),)
#                 for i in range(a, b+1)
#                 for s in (str(i),)
#                 for length in (len(s),)
#                 for seq_len in range(1, length // 2 + 1)
#                 if i not in invalids and length % seq_len == 0 and len(set([s[seq_len*n:seq_len*(n+1)] for n in range(0, length // seq_len)])) == 1
#             ]
#         )
#     )[-1]
# )

# invalids = set()
# total = 0
# for line in open(0).read().split(','):
#     a, b = map(int, line.split('-'))
#     for i in range(a, b+1):
#         s = str(i)
#         length = len(s)
#         for seq_len in range(1, length // 2 + 1):
#             if i in invalids: break
#             if length % seq_len != 0: continue
#             if len(set([s[seq_len*n:seq_len*(n+1)] for n in range(0, length // seq_len)])) == 1:
#                 total += i
#                 invalids.add(i)
# print(total)
