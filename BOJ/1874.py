from collections import deque

n = int(input())
target_seq = deque()
for _ in range(n):
  target_seq.append(int(input()))

res = []
stack = []
for i in range(1, n + 1):
  while stack and stack[-1] == target_seq[0]:
    res.append('-')
    stack.pop()
    target_seq.popleft()

  else:
    res.append('+')
    stack.append(i)

while stack and stack[-1] == target_seq[0]:
  res.append('-')
  stack.pop()
  target_seq.popleft()

if stack or target_seq:
  print('NO')
else:
  for r in res:
    print(r)
