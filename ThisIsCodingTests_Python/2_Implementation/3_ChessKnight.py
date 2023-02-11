loc = input()

col_map = {s:i+1 for i, s in enumerate(list('abcdefgh'))}
directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

loc = [col_map[loc[0]], int(loc[1])]

sol = 0
for direction in directions:
  new_x = loc[0] + direction[0]
  new_y = loc[1] + direction[1]

  if 0<new_x<9 and 0<new_y<9:
    sol += 1

print(sol)
