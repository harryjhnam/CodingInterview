N, M = map(int, input().split())
Ls = list(map(int, input().split()))

Ls.sort()

# def binary_search(Ls, target, start, end):
#   mid = (start + end) // 2
#   retrieved_len = sum([L - mid for L in Ls if L > mid])

#   if retrieved_len == target:
#     return mid
#   elif retrieved_len < target:
#     return binary_search(Ls, target, start, mid - 1)
#   elif retrieved_len > target:
#     return binary_search(Ls, target, mid + 1, end)
#
# ans = binary_search(Ls, M, 0, Ls[N - 1])

ans = None
start, end = 0, max(Ls)

while start <= end:
  mid = (start + end) // 2
  total_len = sum([L - mid for L in Ls if L > mid])

  if total_len >= M:
    ans = mid
    start = mid + 1
  else:
    end = mid - 1

print(ans)
