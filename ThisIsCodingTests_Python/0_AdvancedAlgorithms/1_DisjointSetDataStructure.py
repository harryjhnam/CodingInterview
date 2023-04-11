def find_parent(parent, x):
  # 루트 노드를 찾을 때까지 재귀 호출하며 각 노드의 parent또한 업데이트
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


# 노드의 개수: v, 간선의 개수: e
parent = [i for i in range(v + 1)]

# 간선 정보를 입력 받아 union 연산 수행
for _ in range(e):
  a, b = map(int, input().split())

  # 사이클 판별 가능
  if find_parent(a) == find_parent(b):
    print("사이클 발생!")

  union_parent(parent, a, b)

# 각 원소에 속한 집합 출력하기
for i in range(1, v + 1):
  print(find_parent(parent, i))  # i 노드의 루트 노드 번호를 반환
