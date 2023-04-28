# https://www.acmicpc.net/problem/1011
# Fly me to the Alpha Centauri
from math import sqrt


def solution(dist):
  res = []

  sub_dist = dist - int(sqrt(dist))**2
  cnt = sub_dist // int(sqrt(dist))
  if sub_dist % int(sqrt(dist)) != 0:
    cnt += 1

  res.append(2 * int(sqrt(dist)) - 1 + cnt)

  return min(res)


t = int(input())
res = []
for _ in range(t):
  x, y = map(int, input().split())
  dist = y - x
  if dist < 4:
    res.append(dist)
  else:
    res.append(solution(dist))

for r in res:
  print(r)
