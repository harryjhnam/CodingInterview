# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2

from collections import deque

n, m = map(int, input().split())

is_reachable = []
red, blue, hole = (0, 0), (0, 0), (0, 0)
for i in range(n):
  in_row = list(input())
  row = []
  for j, x in enumerate(in_row):
    if x == '#':
      row.append(False)
    else:
      row.append(True)
      if x == 'B':
        blue = (i, j)
      elif x == 'R':
        red = (i, j)
      elif x == 'O':
        hole = (i, j)

  is_reachable.append(row)


def tilt(is_reachable, dir, orb, hole):
  while True:
    nxt_i, nxt_j = orb[0] + dir[0], orb[1] + dir[1]
    if not is_reachable[nxt_i][nxt_j]:
      break
    orb = (nxt_i, nxt_j)
    if orb == hole:
      orb = -1
      break
  return orb


def solution(is_reachable, red, blue, hole):
  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  q = deque([(dir, red, blue, 0) for dir in dirs])

  while q:

    dir, red, blue, n_moves = q.popleft()

    if n_moves == 10:
      continue

    nxt_red = tilt(is_reachable, dir, red, hole)
    nxt_blue = tilt(is_reachable, dir, blue, hole)

    if nxt_blue == -1:
      continue

    if nxt_red == red and nxt_blue == blue:
      continue

    if nxt_red == -1:
      return n_moves + 1

    if nxt_red == nxt_blue:
      if dir == (0, 1):
        if red[1] < blue[1]:
          nxt_red = (nxt_red[0], nxt_red[1] - 1)
        else:
          nxt_blue = (nxt_blue[0], nxt_blue[1] - 1)
      elif dir == (0, -1):
        if red[1] < blue[1]:
          nxt_blue = (nxt_blue[0], nxt_blue[1] + 1)
        else:
          nxt_red = (nxt_red[0], nxt_red[1] + 1)
      elif dir == (1, 0):
        if red[0] < blue[0]:
          nxt_red = (nxt_red[0] - 1, nxt_red[1])
        else:
          nxt_blue = (nxt_blue[0] - 1, nxt_blue[1])
      elif dir == (-1, 0):
        if red[0] < blue[0]:
          nxt_blue = (nxt_blue[0] + 1, nxt_blue[1])
        else:
          nxt_red = (nxt_red[0] + 1, nxt_red[1])

    for nxt_dir in dirs:
      if nxt_dir == dir:
        continue
      q.append((nxt_dir, nxt_red, nxt_blue, n_moves + 1))

  return -1


print(solution(is_reachable, red, blue, hole))
