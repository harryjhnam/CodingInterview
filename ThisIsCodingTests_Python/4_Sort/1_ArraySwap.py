N, K = map(int, input().split())
A = list( map(int, input().split()) )
B = list( map(int, input().split()) )

A.sort()
B.sort(reverse=True)

ans = 0
for a, b in zip(A[:K], B[:K]):
  ans += b if b>a else a

ans += sum(A[K:])
  
print(ans)
