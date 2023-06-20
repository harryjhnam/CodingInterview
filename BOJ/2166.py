# https://www.acmicpc.net/problem/2166
# 다각형의 면적

n = int(input())
points = []
for _ in range(n):
  points.append(list(map(int, input().split())))


def ccw_term(p1, p2, p3):
  x1, y1 = p1
  x2, y2 = p2
  x3, y3 = p3
  return x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)


res = 0
for i in range(1, n - 1):
  res += ccw_term(points[0], points[i], points[i + 1])

print(0.5 * abs(res))
