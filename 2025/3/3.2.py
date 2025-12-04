print(sum(int((rec := lambda arr, n: max(arr) if n == 1 else (highest := max(arr[:-(n-1)])) + rec(arr[arr.index(highest)+1:], n-1))(line, 12)) for line in open(0).read().split()))


# print(sum(int(
#     (rec := lambda arr, n:
#         max(arr) if n == 1 else
#         (highest := max(arr[:-(n-1)])) + rec(arr[arr.index(highest)+1:], n-1)
#     )(line, 12)
# ) for line in open(0).read().split()))


# def rec(arr, n):
#     if n == 1:
#         return max(arr)
#     highest = max(arr[:-(n-1)])
#     new_arr = arr[arr.index(highest)+1:]
#     return highest + rec(new_arr, n-1)
#
# print(sum(int(rec(line, 12)) for line in open(0).read().split()))
