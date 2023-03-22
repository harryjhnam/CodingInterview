from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
Xs = list(map(int, input().split()))

count = bisect_right(Xs, x) - bisect_left(Xs, x)
if count != 0:
  print(count)
else:
  print(-1)
