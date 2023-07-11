# https://www.acmicpc.net/problem/12100
# 2048 (Easy)

from copy import deepcopy


def swipe_vertical(state, dir='up'):
  n = len(state)
  for col in range(n):

    # shift non-zero tiles
    merge_row = 0 if dir == 'up' else n - 1
    for row in range(n) if dir == 'up' else range(n - 1, -1, -1):
      if state[row][col] != 0:
        tile = state[row][col]
        state[row][col] = 0
        state[merge_row][col] = tile
        merge_row += 1 if dir == 'up' else -1

    # merge adjacent tiles with the same values
    for row in range(n - 1) if dir == 'up' else range(n - 1, 0, -1):
      if dir == 'up' and state[row][col] != 0 and state[row][col] == state[
          row + 1][col]:
        state[row][col] *= 2
        state[row + 1][col] = 0
      if dir == 'down' and state[row][col] != 0 and state[row][col] == state[
          row - 1][col]:
        state[row][col] *= 2
        state[row - 1][col] = 0

    # shift non-zero tiles again
    merge_row = 0 if dir == 'up' else n - 1
    for row in range(n) if dir == 'up' else range(n - 1, -1, -1):
      if state[row][col] != 0:
        tile = state[row][col]
        state[row][col] = 0
        state[merge_row][col] = tile
        merge_row += 1 if dir == 'up' else -1

  return state


def swipe_horizontal(state, dir='left'):
  n = len(state)
  for row in range(n):

    # shift non-zero tiles
    merge_col = 0 if dir == 'left' else n - 1
    for col in range(n) if dir == 'left' else range(n - 1, -1, -1):
      if state[row][col] != 0:
        tile = state[row][col]
        state[row][col] = 0
        state[row][merge_col] = tile
        merge_col += 1 if dir == 'left' else -1

    # merge adjacent tiles with the same values
    for col in range(n - 1) if dir == 'left' else range(n - 1, 0, -1):
      if dir == 'left' and state[row][col] != 0\
          and state[row][col] == state[row][col+1]:
        state[row][col] *= 2
        state[row][col + 1] = 0
      if dir == 'right' and state[row][col] != 0\
          and state[row][col] == state[row][col-1]:
        state[row][col] *= 2
        state[row][col - 1] = 0

    # shift non-zero tiles again
    merge_col = 0 if dir == 'left' else n - 1
    for col in range(n) if dir == 'left' else range(n - 1, -1, -1):
      if state[row][col] != 0:
        tile = state[row][col]
        state[row][col] = 0
        state[row][merge_col] = tile
        merge_col += 1 if dir == 'left' else -1

  return state


def update_state(state, d):
  if d == 0:
    state = swipe_vertical(state, dir='up')
  elif d == 1:
    state = swipe_vertical(state, dir='down')
  elif d == 2:
    state = swipe_horizontal(state, dir='left')
  elif d == 3:
    state = swipe_horizontal(state, dir='right')
  return state


def solution(state, n_move):
  if n_move == 5:
    return max(list(map(max, state)))

  res = []
  for d in range(4):
    res.append(solution(update_state(deepcopy(state), d), n_move + 1))
  return max(res)


n = int(input())
state = []
for _ in range(n):
  li = list(map(int, input().split()))
  state.append(li)

print(solution(state, 0))
