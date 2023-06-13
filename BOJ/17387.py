# https://www.acmicpc.net/problem/17387
# 선분 교차

e = 1e-7


def get_boundary(i1, i2, j1, j2):
  i1, i2 = sorted([i1, i2])
  j1, j2 = sorted([j1, j2])

  if (i2 - i1) + (j2 - j1) < max(i2, j2) - min(i1, j1):
    return None

  m = max(i1, j1)
  M = min(i2, j2)

  return m, M


def get_abc(line):
  x1, y1, x2, y2 = line
  if x1 == x2:
    a = 1
    b = -x1
    c = 0
  else:
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    c = 1
  return a, b, c


def solution(lineA, lineB):

  x_range = get_boundary(lineA[0], lineA[2], lineB[0], lineB[2])
  y_range = get_boundary(lineA[1], lineA[3], lineB[1], lineB[3])

  if x_range == None or y_range == None:
    return False

  Aa, Ab, Ac = get_abc(lineA)
  Ba, Bb, Bc = get_abc(lineB)

  if Aa == Ba:
    return Ab == Bb

  if Ac == 0:
    x = -Ab / Aa
    y = Ba * x + Bb
  elif Bc == 0:
    x = -Bb / Ba
    y = Aa * x + Ab
  else:
    x = -(Ab - Bb) / (Aa - Ba)
    y = Aa * x + Ab

  return x_range[0]-e <= x <= x_range[1]+e\
        and y_range[0]-e <= y <= y_range[1]+e


lineA = list(map(int, input().split()))
lineB = list(map(int, input().split()))
print(int(solution(lineA, lineB)))
