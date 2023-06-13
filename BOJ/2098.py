# https://www.acmicpc.net/problem/2098
# 외판원 순회
# 파이썬 언어 문제로 시간초과, 풀이 자체는 맞음

N = int(input())

graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

inf = int(1e9)
dp = [[inf] * (1 << N) for _ in range(N)]  # (cur_node, visited_bit_mask)

visited_all = (1 << N) - 1


def dfs(x, visited):
  if visited == visited_all:
    if graph[x][0]:
      return graph[x][0]
    else:
      return inf

  if dp[x][visited] != inf:
    return dp[x][visited]

  tmp = dp[x][visited]
  for i in range(1, N):
    if not graph[x][i]:
      continue
    if visited & (1 << i):
      continue

    tmp = min(tmp, dfs(i, visited | (1 << i)) + graph[x][i])

  dp[x][visited] = tmp

  return tmp


print(dfs(0, 1))
