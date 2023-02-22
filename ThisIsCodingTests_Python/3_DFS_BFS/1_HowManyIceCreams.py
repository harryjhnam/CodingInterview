n_rows, n_cols = map(int, input().split())

graph = []
for _ in range(n_rows):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x <= -1 or x >= n_rows or y <= -1 or y >= n_cols:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x+1, y)
    return True
  else:
    return False

result = 0
for i in range(n_rows):
  for j in range(n_cols):
    if dfs(i,j) == True:
      result += 1

print(result)
