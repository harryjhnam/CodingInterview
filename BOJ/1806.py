# https://www.acmicpc.net/problem/1806
# 부분합

n, s = map(int, input().split())
li = list(map(int, input().split()))

cur_s = 0
start = 0
res = 1e9

for end in range(n):

  cur_s += li[end]

  while start <= end:
    if cur_s < s:
      break
    else:
      res = min(res, end - start + 1)
      cur_s -= li[start]
      start += 1

if res == 1e9:
  print(0)
else:
  print(res)
