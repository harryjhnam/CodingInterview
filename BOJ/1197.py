# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리


def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


V, E = map(int, input().split())

parent = [i for i in range(V + 1)]

edges = []
for _ in range(E):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()

res = 0
for cost, a, b in edges:
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    res += cost

print(res)
