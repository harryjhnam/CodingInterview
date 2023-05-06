# https://www.acmicpc.net/problem/2884
# 알람 시계


def time2min(h, m):
  return h * 60 + m


def min2time(m):
  if m < 0:
    return min2time(24 * 60 + m)
  return m // 60, m % 60


h, m = map(int, input().split())
h, m = min2time(time2min(h, m) - 45)

print(h, m)
